# Part 3: Run the node in the background as a tmux session (in-work)

I eventually encountered the problem everytime my computer went to sleep, say on the macbook laptop, the terminal ssh session would break and the node would not run and sync in the background.

I was given advice that an easy fix was to ***"tmux it"*** for running in the background by [@Wael of PIADA Stake Pool founder of Armada Alliance](https://twitter.com/Piada_stakePool).

This was brand new to me and required a bit of an overwhelming learning curve that now seems simple and really is great to know.

In reality, you only need to know about 5 things.

## So what is Tmux?
[Tmux on Github](https://github.com/tmux/tmux) describes their projects as:

>tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached.

Here's a video my super hacker brother shared with me:

[![Tmux has forever changed the way I write code.](https://www.youtube.com/watch?v=DzNmUNvnB04/default.jpg)](https://www.youtube.com/watch?v=DzNmUNvnB04)

In reality, you only need to know the basics, about 5 things, and level up from there.


## Installation

For rpi linux, we can download tmux using pacman that package manager

```bash
sudo pacman -S tmux
```

From here, we'll need some pluggins to make it run smooth and nicely:

Basically, follow the steps from [Github tmux-plugins](https://github.com/tmux-plugins/tpm)

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

Next, create the configuration file

```bash
cd .config
mkdir tmux
cd tmux
touch nano tmux.conf
```

copy the following into tmux.conf per the tpm instructions

```bash
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'github_username/plugin_name#branch'
# set -g @plugin 'git@github.com:user/plugin'
# set -g @plugin 'git@bitbucket.com:user/plugin'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```

Re source the config file so it is recognized.

```bash
tmux source ~/.tmux.conf
```

Finally, run tmux

```bash
tmux  //in terminal
```

Here's a handy cheatsheet for working with tmux:

https://tmuxcheatsheet.com/
