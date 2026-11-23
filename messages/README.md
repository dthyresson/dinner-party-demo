# Local message bus

`inbox/` is the simulated inbox and `outbox/` contains drafts only. These are file-based fixtures, not real email. Your factory can route per-role notifications itself or poll this folder. The injection script writes a new markdown message into `inbox/`.
