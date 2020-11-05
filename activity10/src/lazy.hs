-- type `ghci`
-- load `:l lazy`
-- run  `f 10 (slow 1000000)`
-- run  `f (slow 1000000) 10`

slow 0 = 0
slow n = 1 + slow(n-1)
f a b = a+1
