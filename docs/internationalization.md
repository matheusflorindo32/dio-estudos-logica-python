# Internationalization strategy

## Language model

English is the default repository landing language in `README.md`, making the project's purpose, setup, examples, quality controls, and architecture accessible internationally. `README.pt-BR.md` is a complete Brazilian Portuguese equivalent for DIO evaluators and the primary learner audience.

The executable learning material remains in Brazilian Portuguese. Function names, prompts, examples, tests, and Wiki pages form one coherent introductory curriculum; translating identifiers in place would create duplicate APIs and break the relationship between lessons and tests. Future localized curricula should live in explicit language paths rather than mixing languages inside the same exercise.

## Synchronization contract

When one README changes, reviewers must check the equivalent section in the other language. Both versions must preserve:

- the same supported Python versions and installation process;
- the same learning stages, examples, quality commands, and verified metrics;
- equivalent links to the Wiki, policies, community files, license, and author;
- a visible language switch near the top.

The documents may use natural phrasing rather than sentence-by-sentence literal translation. Factual equivalence is mandatory.

## Stable technical vocabulary

Code identifiers, paths, commands, product names, and tool names are not translated. Terms such as Issue, Pull Request, branch, type hint, lint, smoke test, and coverage may remain in English when that is the clearest convention for the intended audience.

## Future localization

Before adding another language:

1. identify a real learner or contributor audience;
2. assign a maintainer able to review that language;
3. define the canonical source and synchronization process;
4. translate complete learning units, including accessibility text and errors;
5. add automated link and structural checks when the number of locales makes manual review unreliable.

Machine-generated translations must be reviewed by a proficient human before they are presented as official documentation.
