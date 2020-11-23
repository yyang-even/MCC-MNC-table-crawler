" vim-test
let test#python#runner = 'pyunit'
let g:test#python#pyunit#file_pattern = '\v(test_[^/]+|[^/]+_test)\.py$'


" Dispatch
autocmd FileType python let b:dispatch = './scripts/test.sh'

"
" @reference    Quickfix support for Python tracebacks
"               https://vi.stackexchange.com/questions/5110/quickfix-support-for-python-tracebacks
"
autocmd FileType python compiler pyunit
