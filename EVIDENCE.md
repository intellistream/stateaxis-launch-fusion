# Evidence index

- [`issue54-full-mlp-heterogeneous24-r3-npu4/`](evidence/issue54-full-mlp-heterogeneous24-r3-npu4/): retained physical-NPU component evidence. It is cross-arm byte exact and cleanup-clean, but the 4.727% control drift failed the 2% stability gate.
- [`issue54-full-mlp-heterogeneous24-r3-npu4/SHA256SUMS`](evidence/issue54-full-mlp-heterogeneous24-r3-npu4/SHA256SUMS): repository-relative inventory that validates all 43 copied source files. The original `files.sha256` is retained unchanged and still records the StateAxis source paths.
- [`ecpa-contract-20261011/RESULT.json`](evidence/ecpa-contract-20261011/RESULT.json): active Manifest 0.3 / ECPA admission, host hash binding, tests, full worker build, and current evidence boundary.
- [`current-online-blocker-20261013/RESULT.json`](evidence/current-online-blocker-20261013/RESULT.json): current-state audit showing why a fresh ECPA online campaign cannot be launched reproducibly from this container yet.

The historical component cell is inconclusive. Its candidate timing deltas are
preserved rather than promoted. They do not establish a matched real-online
end-to-end benefit, and the active 2026-10-11 identity remains
performance-unqualified pending a fresh sealed run.
