(define sum_ (lambda (x y) (+ x y)))
(define x (sum_ 1 2))
(display (if (= x 10) "it is 10" "it is not 10"))