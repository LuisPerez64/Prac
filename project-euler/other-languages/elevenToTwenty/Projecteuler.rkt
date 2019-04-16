#lang racket
(define % ;; Really rudimentary modulo formula
    (λ (input mod)
      (if (< input mod)
          input
          (% (- input mod) mod))))
(define ^ expt)

(define triangular
  (λ (input)
    (/ (* input (+ 1 input)) 2)))

(define pentagonal
  (λ (input)
    (/ (* input (- (* 3 input) 1)) 2)))

(define hexagonal
  (λ (input)
    (* input (- (* 2 input) 1))))

(define factorial
  (λ (input)
    (if (or (= 1 input) (= 0 input))
        1
        (* input (factorial (- input 1))))))

(define min
  (λ (x y)
    (if (< x y)
        x
        y)))
(define max
  (λ (x y)
    (if (> x y)
        x
        y)))

(define ++ (λ (x) (+ x 1)))
;; Redo this with a stream, and make the stream hold the primes, 
;; and compare againt the primes that are given to the user.
(define lazyIsPrime
  (let divisor 2
    (λ (inputNumber) 
      (if (>= (* divisor divisor) inputNumber)
          #t
          (if (= 0 (remainder inputNumber divisor))
              #f
              (lazyIsPrime inputNumber (++ divisor)))))))
    
(define lazyPrime
  (λ (x) x))
(define fibonacci ;; With basic form f0 = 1 f1 = 1// Problem 25 assumes f1 f2 not f0 f1
  (λ (input) ;; I don't like this this way like at all. Thinking like a normal person not
    (if (or (= 2 input) (= 1 input)) ;; A CS major, is not consistent. Go with the specs you're
        1 ;;Asked for though...
        (+ (fibonacci (- input 1))  (fibonacci (- input 2))))))

;; Stolen from the internets.... I have no idea how this actively works...
(define fib
  (let ([memo '((0 . 0) (1 . 1))])
    (lambda (n)
      (let ([prev-ans (assoc n memo)])
        ( if prev-ans
             (cdr prev-ans)
             (let ([ans (+ (fib (- n 1)) (fib (- n 2)))])
               (set! memo (cons (cons n ans) memo))
               ans))))))
;; Lattice Paths choice point formulat is (a+b) choose a
(define choose
  (λ (input howMany)
    (let ((topHalf (factorial input))
          (bottomHalf (* (factorial howMany)(factorial (- input howMany)))))
      (/ topHalf bottomHalf))))



;; Sum of a numbers numbers 123 ~ 1+2+3 = 6 and so on, works for massive numbers
;; C would have you doing a lot of vector/array manipulation to attain this functionality
;; It cannot house a number as big as 2^100...

;; Uses my implementation of the int instead of floor algorithm. Exponential growth in time
;; Negligible at small numbers, visible past 2^500. Wroks pretty well with no built in
;; function, sans remainder, since my % function is not efficient at all for numbers past
;; 10e12 if mod is 10... takes about 15 seconds to compute that. While remainder is instant
(define sumMeLessEfficient
  (λ (input)
    (if (< input 10) 
        (int input)
        (+ (remainder (int input) 10) (sumMe (/ input 10))))))

;; Using the inherent functions remainder and floor. Unlike my (cast int) func floor is 
;; instantenous. This follows thorugh on the formula, and calculates the output within 
;; less than a second for (2^1000). Built in functions for the masses, built myself functions
;; for learning.
(define sumMe
  (λ (input)
    (if (< input 10) 
        (floor input)
        (+ (remainder (floor input) 10) (sumMe (/ input 10))))))

;; Supplemented the below with the floor function... 
;; Still want to implement this in my own way efficiently...
;;Initial:
;; Conversion of float into an integer. Ugly and inefficient but works for now.
;; Horribly inefficient. I will make the remainder function work better.
;; Updated:
;; Made it a bit less inefficient, can make it even more efficient with some 
;; finagling, but since its an inherent function in (floor / ceiling) I don't think I can
;; at the moment make a better algorithm than the people who do this for a living -_-
(define int 
    (λ (input)
      (- input (rem input))))

;; Attains the remaining fraction left over after subtracting the 
(define rem
  (λ (input)
    (if (< input 1)
        input
        (rem (- input (maxPowerTwo input 0))))))

;; Increment the counter and get the highest power of Two attainable within the given input
;; This will cut the computation time ridiculously, from the input -1 method
(define maxPowerTwo ;;Scales by powers of Two to exponentially cut down in time needed
  (λ (input counter) ;; Counter will always start at 0, may be able to make this better...
    (if (<= input (expt 2 counter)) 
        (if (= 0 counter) ;; Validation, needed to make sure that we do not attain (2 ^-1)
            1 ;; If that is attained then we are at the lowest possible point, function end
            (^ 2 (- counter 1)));; Decrement the counter to get the number prior
        (maxPowerTwo input (+ 1 counter)))));; Iterative call, no stack overflow.

(define maxTerm (expt 10 1000)) ;; 1000 digit number
;; 1000-digit fibonacci
(define digitCount
  (λ (input count)
    (if (<= (/ input 10) 1)
        (+ 1 count)
        (digitCount (/ input 10) (+ 1 count)))))

(define fibIndex
    (λ (startingIndex internDigitCount)
      (if (>= (digitCount (fib startingIndex) 0) internDigitCount)
          startingIndex
          (fibIndex (+ startingIndex 1)internDigitCount))))

(define t triangular)
(define p pentagonal)
(define h hexagonal)
