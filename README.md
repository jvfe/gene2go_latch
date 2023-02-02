## gene2GO

This is a workflow that queries [HumanMine.org](https://www.humanmine.org/humanmine),
acquiring Gene Ontology IDs that are related to an input gene - and how they're
related.

This requires setting up an API token on HumanMine
([see instructions](http://intermine.org/im-docs/docs/web-services/authentication/#authentication-for-existing-user-accounts-permanent-tokens))
and setting this input token as one of your secrets (named **HUMANMINE_TOKEN**)

- see the [Latch tutorial on how to set up secrets](https://docs.latch.bio/basics/adding_secrets.html?highlight=secret)
