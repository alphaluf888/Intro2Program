;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1_2functions-and-programs) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
;Exercise 11. 
;Define a function that consumes two numbers, x and y, and 
;that computes the distance of point (x,y) to the origin.

(define (distance x y)
  (sqrt (+ (* x x) 
           (* y y))))


;Exercise 12. 
;Define the function cvolume, which accepts the 
;length of a side of an equilateral cube and computes its 
;volume. If you have time, consider defining csurface, too.

(define (cvolume x)
  (* x x x))

(define (csurface x)
  (* 6 x x))


;Exercise 13. 
;Define the function string-first, which extracts the first 
;1String from a non-empty string. Don’t worry about empty strings.

(define (string-first s)
  (substring s 0 1))


;Exercise 14. 
;Define the function string-last, which extracts the last 1String 
;from a non-empty string. Don’t worry about empty strings.

(define (string-last s)
  (substring s (- (string-length s) 1)))

;Exercise 15. 
;Define ==>. The function consumes two Boolean values, call them 
;sunny and friday. The answer of the function is #true if sunny 
;is false or friday is true. Note Logicians call this Boolean 
;operation implication, and they use the notation sunny => friday
;for this purpose. 

(define (==> sunny friday)
  (or (not sunny) friday))




