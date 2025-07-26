# Daily Gist

This repository uses a GitHub Actions workflow to pin a random gist to your GitHub profile every day.

## How it works
- A Python script fetches your gists, selects one at random, and pins it to your profile.
- The workflow runs daily using GitHub Actions.

## Setup
1. Fork or clone this repository.
2. Add a `GH_TOKEN` secret to your repository with a GitHub token that has `gist` and `read:user` permissions.

## Customization
- You can modify the script in `pin_random_gist.py` to change how the gist is selected or pinned.

## License
MIT
