from latch.types.metadata import (
    LatchAuthor,
    LatchMetadata,
    LatchParameter,
    Params,
    Section,
    Text,
)

PARAMS = {
    "gene_name": LatchParameter(
        display_name="Gene Symbol",
        batch_table_column=True,
    ),
}

FLOW = [
    Section(
        "Gene Name",
        Text(
            "Gene name must follow [HUGO](https://www.genenames.org/)"
            " nomenclature, e.g. 'BRCA1' or 'PPARG'"
        ),
        Params("gene_name"),
    )
]

WORKFLOW_NAME = "gene2GO"

wf_docs = LatchMetadata(
    display_name=WORKFLOW_NAME,
    documentation=f"https://github.com/jvfe/{WORKFLOW_NAME}_latch/blob/main/README.md",
    author=LatchAuthor(
        name="jvfe",
        github="https://github.com/jvfe",
    ),
    repository=f"https://github.com/jvfe/{WORKFLOW_NAME}_latch",
    license="MIT",
    parameters=PARAMS,
    tags=["Gene Ontology", "HumanMine"],
    flow=FLOW,
)
