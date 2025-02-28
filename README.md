# Simple_Ci_CD_Calculator


# Simple-Calculator

Please copy and paste this in your hooks --->Prepare-commit-msg and deleate .sample in the file name

#!/bin/sh
# #
# # An example hook script to prepare the commit log message.
# # Called by "git commit" with the name of the file that has the
# # commit message, followed by the description of the commit
# # message's source.  The hook's purpose is to edit the commit
# # message file.  If the hook fails with a non-zero status,
# # the commit is aborted.
# #
# # To enable this hook, rename this file to "prepare-commit-msg".
# # This hook includes three examples. The first one removes the
# # "# Please enter the commit message..." help message.
# #
# # The second includes the output of "git diff --name-status -r"
# # into the message, just before the "git status" output.  It is
# # commented because it doesn't cope with --amend or with squashed
# # commits.
# #
# # The third example adds a Signed-off-by line to the message, that can
# # still be edited.  This is rarely a good idea.
# COMMIT_MSG_FILE=$1
# COMMIT_SOURCE=$2
# SHA1=$3
# /usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"
# # case "$COMMIT_SOURCE,$SHA1" in
# #  ,|template,)
# #    /usr/bin/perl -i.bak -pe '
# #       print "\n" . `git diff --cached --name-status -r`
# #      if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
# #  *) ;;
# # esac
# # SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# # git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# # if test -z "$COMMIT_SOURCE"
# # then
# #   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# # fi
# #!/bin/sh
# #
# # An example hook script to verify what is about to be committed.
# # Called by "git commit" with no arguments.  The hook should
# # exit with non-zero status after issuing an appropriate message if
# # it wants to stop the commit.
# #
# # To enable this hook, rename this file to "pre-commit".
# if git rev-parse --verify HEAD >/dev/null 2>&1
# then
#   against=HEAD
# else
#   # Initial commit: diff against an empty tree object
#   against=$(git hash-object -t tree /dev/null)
# fi
# # If you want to allow non-ASCII filenames set this variable to true.
# allownonascii=$(git config --type=bool hooks.allownonascii)
# # Redirect output to stderr.
# exec 1>&2
# # Cross platform projects tend to avoid non-ASCII filenames; prevent
# # them from being added to the repository. We exploit the fact that the
# # printable range starts at the space character and ends with tilde.
# if [ "$allownonascii" != "true" ] &&
#   # Note that the use of brackets around a tr range is ok here, (it's
#   # even required, for portability to Solaris 10's /usr/bin/tr), since
#   # the square bracket bytes happen to fall in the designated range.
#   test $(git diff --cached --name-only --diff-filter=A -z $against |
#     LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
# then
#   cat <<\EOF
# Error: Attempt to add a non-ASCII file name.
# This can cause problems if you want to work with people on other platforms.
# To be portable it is advisable to rename the file.
# If you know what you are doing you can disable this check using:
#   git config hooks.allownonascii true
# EOF
#   exit 1
# fi
# # If there are whitespace errors, print the offending file names and fail.
# exec git diff-index --check --cached $against --
#!/usr/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".
# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"
# This example catches duplicate Signed-off-by lines.
HOOK_FILE=$1
COMMIT_MSG=`head -n1 $HOOK_FILE`
# PATTERN="^[A-Z][A-Z0-9]+-[0-9]+"
PATTERN="^SC+-[0-9]+"
if [[ ! ${COMMIT_MSG} =~ $PATTERN ]]; then
  echo ""
  echo "    ERROR! Bad commit message. "
  echo "    '$COMMIT_MSG' is missing JIRA Ticket Number."
  echo "    example: 'SC-1234: my commit'"
  echo ""
  exit 1
fi