"""Agent example: generate example-style OpenCAD code for a mounting bracket."""

from __future__ import annotations

import os

from opencad_agent.models import ChatRequest
from opencad_agent.service import OpenCadAgentService
from opencad_tree.models import FeatureNode, FeatureTree


def _seed_tree() -> FeatureTree:
    return FeatureTree(
        root_id="root",
        nodes={
            "root": FeatureNode(
                id="root",
                name="Root",
                operation="seed",
                parameters={},
                depends_on=[],
                status="built",
                shape_id=None,
            )
        },
    )


def _optional_llm_settings() -> tuple[str | None, str | None]:
    provider = os.getenv("OPENCAD_LLM_PROVIDER")
    model = os.getenv("OPENCAD_LLM_MODEL")
    if provider and not model:
        raise SystemExit("Set OPENCAD_LLM_MODEL when OPENCAD_LLM_PROVIDER is configured.")
    return provider, model


def main() -> None:
    provider, model = _optional_llm_settings()
    service = OpenCadAgentService()
    response = service.chat(
        ChatRequest(
            message="Generate a mounting bracket script with corner fasteners and a center cutout",
            tree_state=_seed_tree(),
            conversation_history=[],
            reasoning=True,
            generate_code=True,
            llm_provider=provider,
            llm_model=model,
        )
    )
    print(response.generated_code or response.response)


if __name__ == "__main__":
    main()
