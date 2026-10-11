"""Sealed physical-B32 full-MLP launch fusion activation contract."""

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-launch-fusion"


@dataclass(frozen=True, slots=True)
class LaunchFusionConfig:
    enabled: bool = True
    scope: str = "qwen2.5-14b-bf16-physical-b32-full-mlp"
    decode_mlp_policy: str = "full_mlp_pto_b32_split_sealed"
    physical_batch: int = 32
    sealed_component_required: bool = True
    closure_hash_required: bool = True
    workspace_bytes: int = 1_769_472
    workspace_alignment: int = 512
    non_b32_fallback: str = "aclnn_fused_gate_up_swiglu_and_down"
    exact_output_required: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "scope": "qwen2.5-14b-bf16-physical-b32-full-mlp",
            "decode_mlp_policy": "full_mlp_pto_b32_split_sealed",
            "physical_batch": 32,
            "sealed_component_required": True,
            "closure_hash_required": True,
            "workspace_bytes": 1_769_472,
            "workspace_alignment": 512,
            "non_b32_fallback": "aclnn_fused_gate_up_swiglu_and_down",
            "exact_output_required": True,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError("launch fusion requires the reviewed sealed contract")


def launch_fusion() -> LaunchFusionConfig:
    return LaunchFusionConfig()


__all__ = ["MOD_ID", "LaunchFusionConfig", "launch_fusion"]
