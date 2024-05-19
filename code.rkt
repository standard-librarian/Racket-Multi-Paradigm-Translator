(define average (lambda (lst) (/ (foldl (lambda (x y) (+ x y)) 0 lst) (length lst))))
(display (average (list 1 2 3)))