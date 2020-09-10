" vim-test
let test#python#runner = 'pyunit'
let g:test#python#pyunit#file_pattern = '\v(test_[^/]+|[^/]+_test)\.py$'


" Dispatch
"autocmd FileType python let b:dispatch = './scripts/test.sh'
autocmd FileType python let b:dispatch = 'pipenv run python3 -m unittest %'
