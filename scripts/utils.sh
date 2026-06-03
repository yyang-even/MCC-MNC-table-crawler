QuietRun() {
    "$@" > /dev/null
}

GetProjectRootDir() {
    git rev-parse --show-toplevel
}
