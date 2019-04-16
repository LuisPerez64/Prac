#lang racket
;; Honestly don't believe that this could be done in CPP, number is way too large.
(define selfPowers
  (λ (lowerLimit upperLimit init)   
    (if (> lowerLimit upperLimit)
        init
        (selfPowers (+ 1 lowerLimit) upperLimit (+ init (expt lowerLimit lowerLimit))))))


;; Long way of getting the prime.
(define isPrime? 
  (λ (base divisor)
    (if (= divisor base)
        #t
        (if (= (remainder base divisor) 0)
            #f
            (isPrime? base (+ divisor 1))))))

(define isPrimeBetter
  (λ (base divisor listOfPrimes)
    base))