# StateAxis Launch Fusion

Extension ID: `org.vllm-hust.stateaxis-launch-fusion`

This MOD is the active, default-off ECPA boundary for StateAxis issue
[#54](https://github.com/Qixin-Gaoke/stateaxis/issues/54). It admits exactly the
reviewed Qwen2.5-14B BF16 physical-B32 full-MLP policy, requires the sealed PTO
component and closure identity, and fails closed on every altered field.

## Activation

The MOD is activated only through vLLM-HUST Extension Manager/ECPA. The
StateAxis host validates the exact Manifest 0.3 payload and
`RESEARCH_MANIFEST.json` SHA-256, fingerprints the identity into the assembly,
and emits applied-candidate telemetry only when the sealed B32 path dispatches.
Direct ambient selection of `full_mlp_pto_b32_split_sealed` is rejected.

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-launch-fusion
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```

Rollback is to disable the extension. The host then retains the ACLNN fused
Gate/Up-SwiGLU-and-Down fallback and refuses the sealed policy.

## Evidence boundary

The retained physical-B32 component probe was cross-arm byte exact. Candidate
device-event time improved 14.213% and host total time improved 16.939%, but
control drift was 4.727%, above the 2% stability limit. The component result is
therefore **inconclusive** and does not establish a real-online or general
speedup. The current active Host/MOD identity has not received a fresh matched
online run and remains performance-unqualified. The 2026-10-13 environment audit
found an idle NPU but no official runtime-image launcher or fresh sealed artifact
bound to the current Host/MOD identity; the occupied NPU was left untouched. See
[EVIDENCE.md](EVIDENCE.md) for the reproducible blocker and evidence inventory.

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
