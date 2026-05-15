# Agent Examples

This repository includes one agent-driven script generator:

- `examples/agents/generate_mounting_bracket_code.py`

## Default run (no extra setup)

```bash
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```

## Use a LiteLLM-backed provider

```bash
export OPENCAD_LLM_PROVIDER=openai
export OPENCAD_LLM_MODEL=gpt-4o-mini
python examples/agents/generate_mounting_bracket_code.py > generated_bracket.py
```

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
