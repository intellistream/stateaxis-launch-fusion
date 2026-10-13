# Current real-online blocker — 2026-10-13

The active ECPA contract is valid, and physical NPU5 was idle at inspection time.
The campaign was not started because the current StateAxis runtime integration has
no qualified runtime image or build-source closure, this container has neither a
Docker nor sudo launcher, and no fresh sealed full-MLP artifact bound to the active
Host/MOD identity was present under `/data`, `/root/stateaxis` or
`/root/stateaxis-evidence`.

Physical NPU4 was occupied by an existing `VLLMEngineCor` process and was not
disturbed. No process was terminated and no NPU workload was launched.

This is a reproducible environment/artifact blocker, not a performance result.
The historical component campaign remains independently valid and inconclusive.
Recovery requires a source-closure-qualified sealed artifact plus a qualified image
or equivalent launcher, followed by an interleaved fresh-process ECPA OFF/ON serving
campaign with exactness, activation telemetry, lifecycle and bracket-stability gates.
