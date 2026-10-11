# Active ECPA contract — 2026-10-11

This directory records activation and build validation for release `0.2.0`.
The StateAxis host at `320ddd2dbba503c50c5f940d069f4d3e09e76a61`
accepts only the exact research-manifest digest through ECPA, fingerprints the
MOD identity into the assembly, rejects direct ambient selection of the sealed
policy, and reports candidate batches only after actual sealed B32 dispatch.

The retained real-NPU component probe remains inconclusive because its control
drift failed the stability gate. No fresh matched online run was made for this
new Host/MOD identity, so the current release is not performance-qualified.
