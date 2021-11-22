# dotfiles

Check [here](https://www.atlassian.com/git/tutorials/dotfiles) to see how to setup.

## TD;DR

### Starting from scratch

```
git init --bare $HOME/.dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
echo "alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.bashrc
```

### Clone to new system

```
echo "alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.bashrc
echo ".dotfiles" >> .gitignore
# git clone --bare <git-repo-url> $HOME/.dotfiles
git clone --bare https://github.com/dmse/dotfiles.git $HOME/.dotfiles
dotfiles checkout
```

NOTE: reload terminal or run `alias dotfiles` command again for the current shell
