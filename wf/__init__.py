from pathlib import Path

import requests
from latch import medium_task, workflow
from latch.functions.secrets import get_secret
from latch.resources.launch_plan import LaunchPlan
from latch.types import LatchFile

from .docs import wf_docs


@medium_task
def gene2GO_task(gene_name: str) -> LatchFile:
    """Task to query HumanMine"""

    token = get_secret("HUMANMINE_TOKEN")

    results_path = "query_results.tsv"
    output_file = Path(results_path).resolve()

    base_url = "https://www.humanmine.org/humanmine/service/template/results"

    params = {
        "name": "Gene_GO",
        "constraint1": "Gene",
        "op1": "LOOKUP",
        "value1": gene_name,
        "extra1": "H. sapiens",
        "format": "tab",
        "token": token,
    }

    response = requests.get(base_url, params=params)

    with open(output_file, "w") as f:

        header = [
            "GeneID",
            "Symbol",
            "GO_ID",
            "GO_Term",
            "GO_Category",
            "Code",
            "Parent_GO_ID",
            "Parent_Go_Term",
            "GO_Qualifier",
        ]

        header_string = "\t".join(header) + "\n"

        f.write(header_string)
        f.write(response.text)

    return LatchFile(str(output_file), f"latch:///gene2GO/{gene_name}_results.tsv")


@workflow(wf_docs)
def gene2GO(gene_name: str) -> LatchFile:
    """Get Gene Ontology terms related to a Human Gene

    gene2GO
    ------

    This is a workflow that queries [HumanMine.org](https://www.humanmine.org/humanmine),
    acquiring Gene Ontology IDs that are related to an input gene - and how they're
    related.

    This requires setting up an API token on HumanMine
    ([see instructions](http://intermine.org/im-docs/docs/web-services/authentication/#authentication-for-existing-user-accounts-permanent-tokens))
    and setting this input token as one of your secrets (named **HUMANMINE_TOKEN**)
    - see the [Latch tutorial on how to set up secrets](https://docs.latch.bio/basics/adding_secrets.html?highlight=secret)

    """
    return gene2GO_task(gene_name=gene_name)


LaunchPlan(
    gene2GO,
    "BRCA1-related GO terms",
    {"gene_name": "BRCA1"},
)
