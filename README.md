# CORRAL

CORRAL corrals every scattered tmux session and running job across your SSH/Slurm nodes into one live pane. It automatically discovers the compute nodes allocated to you, scans each one for active tmux sessions and job state, and gives you a single dashboard to monitor, attach, kill, or annotate any of them without ever leaving the terminal.

## Features

- **Automatic Node Discovery**: Queries `squeue` to find all compute nodes currently allocated to your user.
- **Session Scanning**: Connects to each node via SSH to list active tmux sessions.
- **Split-View Dashboard**: Compact session list on the left, live snapshot preview on the right.
- **Job-Aware**: Each row is annotated with its Slurm job -- JobID, name, partition, state, and time remaining.
- **Mouse Support**: Click rows to select, use mouse wheel to scroll.
- **Watch Mode**: Set an inactivity alert (`w`) on any session to get notified if it hangs or stops updating.
- **Slack Notifications**: Receive real-time alerts in your Slack channel when a watched session becomes inactive. (Config via `S`).
- **Live Refresh**: Sessions are automatically re-scanned in the background every 30 seconds. (Press `r` to force refresh).
- **Session Management**:
  - **Attach**: Instantly attach to any tmux session or start a new shell.
  - **Create (`c`)**: Create new named sessions on any node directly from the UI.
  - **Kill (`k`)**: Terminate sessions with a confirmation prompt.
- **Search / Filter (`/`)**: Quickly filter the session list by typing queries.
- **One-Key Connection**:
  - **Attach**: Instantly attach to any tmux session with `ENTER`.
  - **Shell**: Open a fresh shell on any active node with `s`.
- **Persistent Notes**: Add custom notes to any session (`n` key) to keep track of experiment status or to-do items. Notes are saved to `~/.corral_notes.json`.
- **Persistent Snapshots**: Snapshots are automatically captured and saved to `~/.corral_snapshots.json` so they are available instantly and across restarts.
- **Error Logging (`e`)**: View connection errors and issues directly within the tool.
- **Stale Session Tracking**: Keeps track of sessions you've noted even if they go offline (displayed in red).

## Installation

You can install CORRAL directly from the source:

```bash
git clone <your-repo-url>
cd corral
pip install .
```

Or run it directly without installation:

```bash
python3 corral.py
```

## Usage

Start the application by running:

```bash
corral
```

### Dashboard Controls

| Key | Action |
| :--- | :--- |
| **UP / DOWN** | Navigate the list of sessions. |
| **ENTER** | **Attach** to the selected tmux session via SSH. |
| **s** | Open a raw SSH **shell** on the selected node. |
| **r** | **Refresh** the session list. |
| **k** | **Kill** the selected session (with confirmation). |
| **c** | **Create** a new session on a specific node. |
| **w** | **Watch** the selected session for inactivity. |
| **/** | **Search / Filter** the list. |
| **n** | **Add/Edit Note** for the selected session. |
| **d** | **Delete Note** (and remove from list if session is offline). |
| **S** | **Settings** (Slack webhook, refresh interval). |
| **e** | **View Error Log**. |
| **?** | **Show Help** screen. |
| **q** | **Quit** the application. |

## Requirements

- **Python 3.6+**
- **Slurm**: The tool uses `squeue` to find nodes.
- **SSH**: Must have SSH access to compute nodes (configured with keys for passwordless access recommended).
- **Tmux**: Must be installed on the remote nodes.

## Configuration

CORRAL stores your session notes in `~/.corral_notes.json`. You can manually edit this file if needed, but it is managed automatically by the application. Snapshots, cached node state, and settings (including your Slack webhook) live alongside it in `~/.corral_snapshots.json`, `~/.corral_cache.json`, and `~/.corral_config.json`.
