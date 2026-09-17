# Contributing

## Development expectations

Keep changes focused, document user-visible behavior and include tests for new application rules. Do not commit secrets, local databases, dependency folders or generated build output.

Before opening a pull request, run:

```bash
cd backend
ruff check .
pytest
```

```bash
cd frontend
npm run lint
npm test
npm run build
```

Describe the problem, the implementation decision, verification performed and any remaining limitations in the pull request.

