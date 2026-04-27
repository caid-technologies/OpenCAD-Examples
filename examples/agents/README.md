# OpenCAD Agent Examples

These examples show how to use the OpenCAD agent's code-generation mode.

## Included scripts

- `generate_mounting_bracket_code.py` — requests an example-style mounting bracket script from the agent

## Running the example

From the repository root:

```bash
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```

By default, the script uses the built-in deterministic generator so it runs without extra setup.

To use a LiteLLM-backed provider instead, set provider/model environment variables before running:

```bash
export OPENCAD_LLM_PROVIDER=openai
export OPENCAD_LLM_MODEL=gpt-4o-mini
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```

Provider credentials continue to come from the provider's standard environment variables.

## Claude example

```bash
export OPENCAD_LLM_PROVIDER=anthropic
export OPENCAD_LLM_MODEL=claude-3-5-sonnet-latest
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```

## Gemini example

```bash
export OPENCAD_LLM_PROVIDER=gemini
export OPENCAD_LLM_MODEL=gemini-2.0-flash
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```
