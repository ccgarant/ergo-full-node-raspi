# Part 3: Run the node in the background as a tmux session (in-work)

I eventually encountered the problem everytime my computer went to sleep, the terminal ssh session would break and the node would not run and sync in the background.

I was given advice that an easy fix was to "tmux it" for running in the background. 

This was brand new to me and required a bit of an overwhelming learning curve that now seems simple and really is great to know.



https://www.youtube.com/watch?v=DzNmUNvnB04

https://github.com/tmux/tmux

sudo pacman -S tmux

https://github.com/tmux-plugins/tpm

git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

cd .config
mkdir tmux
cd tmux
echo " " > tmux.conf
nano tmux.conf

copy the following into tmux.conf per the tpm instructions

```
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

#run tmux
tmux  //in terminal

# type this in terminal if tmux is already running
tmux source ~/.tmux.conf

https://tmuxcheatsheet.com/
