class DefaultColor:
    """
    This class should have the default colors for every segment.
    Please test every new segment with this theme first.
    """
    USERNAME_FG = 15
    USERNAME_BG = 240
    USERNAME_ROOT_BG = 124

    HOSTNAME_FG = 15
    HOSTNAME_BG = 238

    HOME_SPECIAL_DISPLAY = False
    HOME_BG = 237  # blueish
    HOME_FG = 231  # white
    PATH_BG = 31  # dark grey
    PATH_FG = 231  # light grey
    CWD_FG = 231  # white
    SEPARATOR_FG = 237

    READONLY_BG = 124
    READONLY_FG = 254

    SSH_BG = 166 # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 22 # a light green color
    REPO_CLEAN_FG = 231  # white
    REPO_DIRTY_BG = 161  # pink/red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 39
    JOBS_BG = 238

    CMD_PASSED_BG = 31
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 161
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 15  # dark green

    GIT_AHEAD_BG = 98
    GIT_AHEAD_FG = 231
    GIT_BEHIND_BG = 88
    GIT_BEHIND_FG = 231
    GIT_STAGED_BG = 22
    GIT_STAGED_FG = 231
    GIT_NOTSTAGED_BG = 220
    GIT_NOTSTAGED_FG = 0
    GIT_UNTRACKED_BG = 52
    GIT_UNTRACKED_FG = 231
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = 231

    VIRTUAL_ENV_BG = 35  # a mid-tone green
    VIRTUAL_ENV_FG = 15

class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass
