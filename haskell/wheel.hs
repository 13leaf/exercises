--Data.Function
on' :: (b->b->c)->(a->b) -> a -> a -> c
f `on'` g = \x y -> f (g x) (g y)

-- Data.Maybe
isNothing' :: Maybe a -> Bool
isNothing' Nothing = True
isNothing' _ = False

fromJust' :: Maybe a -> a
fromJust' Nothing = error "from Nothing"
fromJust' (Just a) = a
-- fromJust' (Just 4) = 4

succ' :: Num a => a -> a
succ' x = x + 1
-- succ' 4
-- 5

not' :: Bool -> Bool
not' True = False
not' False = True

negate' :: Num a => a -> a
negate' x =  (-x)

min' :: Ord a => a -> a -> a
min' x y = if x < y then x else y
-- min' 3 4
-- 3

max' :: Ord a => a -> a -> a
max' x y = if x > y then x else y
-- max' 3 4
-- 4

-- [1,2,3] !! 0 取得第0个元素
-- 1:[2,3] 等同于 [1,2,3]

head' :: [a] -> a
head' [] = error "empty list"
head' (x:_) = x

last' :: [a] -> a
last' [x] = x
last' (x:xs) = last' xs

init' :: [a] -> [a]
init' [x] = []
init' (x:xs) = x : init' xs
-- init' [1,2,3]
-- [1,2]

tail' :: [a] -> [a]
tail' xs = case xs of [] -> error "empty list"
                      (_:xs) -> xs
-- tail' [1,2,3]
-- [2,3]

length' :: [a] -> Int
length' xs = sum [1 | _ <- xs]
{-
length' [] = 0
length' (x:xs) = (length' xs) + 1
-}

null' :: [a] -> Bool
null' [] = True
null' _ = False

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

take' :: Int -> [b] -> [b]
take' 0 _ = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs

drop' :: Int -> [a] -> [a]
drop' _ [] = []
drop' n all@(x:xs)
    | n<=0 = all
    | otherwise = drop' (n-1) xs

maximum' :: Ord a => [a] -> a
{-

maximum' (x:[]) = x
maximum' (x:y:xs)
    | x>y = maximum' (x:xs)
    | otherwise = maximum' (y:xs)
-}
maximum' [] = error "empty list"
maximum' [x] = x
maximum' (x:xs)
    | x > maxTail = x
    | otherwise = maxTail
    where maxTail = maximum' xs

sum' :: Num a => [a] -> a
sum' [] = 0
sum' (x:xs) = x + (sum' xs)

elem' ::Eq a => a -> [a] -> Bool
elem' _ [] = False
elem' p (x:xs) = if p == x then True else elem' p xs

notElem' :: Eq a => a -> [a] -> Bool
notElem' x xs = not' $ elem' x xs

cycle' :: [a] -> [a]
cycle' a = a ++ cycle' a

repeat' :: a -> [a]
repeat' a = a:repeat' a

fst' :: (a,b) -> a
fst' (a,_) = a

snd' :: (a,b) -> b
snd' (_,b) = b

zip' :: [a] -> [b] -> [(a,b)]
zip' [] _ = []
zip' (a:as) (b:bs) = (a,b):zip' as bs

compare' :: Ord a => a ->a -> Ordering
compare' x y
    | x == y = EQ
    | x > y = GT
    | otherwise = LT

replicate' :: (Num i,Ord i) => i -> a -> [a]
replicate' n x
    | n <= 0 = []
    | otherwise = x: replicate' (n-1) x
-- replicate' 3 4
-- [3,3,3,3]

sortBy' :: (a->a->Ordering)-> [a]->[a]
sortBy' _ [] = []
sortBy' f (x:xs) =
    let smallSortList = sortBy' f (filter' (\a->f a x /= GT) xs)
        largerSortList = sortBy' f (filter' (\a->f a x == GT) xs)
    in smallSortList ++ [x] ++ largerSortList

sort' :: Ord a => [a]->[a]
sort' = sortBy' compare'

applyTwice:: (a -> a)-> a -> a
applyTwice f x = f (f x)

zipWith' :: ( a -> b -> c ) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' f (a:as) (b:bs) = f a b:zipWith' f as bs
-- zipWith' (+) [1..3] [3,2..1]
-- [4,4,4]

flip' :: (a->b->c) -> b -> a ->c
--flip' f y x = f x y
flip' f = \x y -> f y x

map' :: (a->b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a->Bool) -> [a] -> [a]
--filter' f xs = [ x | x<-xs,f x ]
filter' _ [] = []
filter' f (x:xs) = if f x then x:filter' f xs else filter' f xs

odd' :: (Integral a) => a -> Bool
odd' x = not (x `mod` 2 == 0)

even' :: (Integral a) => a -> Bool
even' x = x `mod` 2 == 0

foldl' :: (b->a->b) -> b -> [a] -> b
foldl' _ init [] = init
foldl' f init (x:xs) = let acc = f init x
                        in foldl' f acc xs

foldl1' :: (a->a->a) -> [a] -> a
foldl1' f (x:xs) = foldl' f x xs

foldr' :: (b->a->b) -> b -> [a] -> b
foldr' _ init [] = init
foldr' f init [x] = f init x
foldr' f init (x:xs) = f (foldr' f init xs) x

foldr1' :: (a->a->a) -> [a] -> a
foldr1' f xs = foldr' f (last' xs) (init' xs)

scanl' :: (b->a->b) -> b -> [a] -> [b]
scanl' f init xs = reverse' $ foldl' (\all@(x:_) a -> f x a : all ) [init] xs

scanr' :: (b->a->b) -> b -> [a] -> [b]
scanr' f init xs = foldr' (\all@(x:_) a -> f x a : all ) [init] xs

scanl1' :: (a->a->a) -> [a] -> [a]
scanl1' f (x:xs) = scanl' f x xs

scanr1' :: (a->a->a) -> [a] -> [a]
scanr1' f xs = scanr' f (last' xs) (init' xs)

gcd' :: Integral a => a -> a -> a
gcd' a b
    | a == b = a
    | a > b = gcd' (a - b) b
    | otherwise = gcd' a (b - a)

lcm' :: Integral a => a -> a -> a
lcm' a b = (a * b) `div` (gcd' a b)

--Data.List
intersperse' :: a -> [a] -> [a]
intersperse' _ [x] = [x]
intersperse' delimit (x:xs) = foldl' (\acc x-> acc ++ [delimit] ++ [x]) [x] xs
-- intersperse' ',' "123"
-- "1,2,3"

intercalate' :: [a] -> [[a]] -> [a]
intercalate' _ [x] = x
intercalate' delimit xs = foldl1' (\acc x -> acc ++ delimit ++ x) xs
-- intercalate' "," ["abc","def"]
-- "abc,def"

transpose' :: [[a]] -> [[a]]
transpose' xs@(x:_) = let n = length' x
                    in [map' (\x -> x !! i) xs | i<-[0..n-1]]

concat' :: [[a]] -> [a]
concat'=foldl1' (++)

concatMap' :: (a->[b]) -> [a] -> [b]
concatMap' f xs = concat' $ map' f xs
-- concatMap' (replicate' 3) [1..3]
-- [1,1,1,2,2,2,3,3,3]

and' :: [Bool] -> Bool
and' = foldl' (&&) True

or' :: [Bool] -> Bool
or' = foldl' (||) False

any' :: (a->Bool) -> [a] -> Bool
any' f xs= or' $ map' f xs

all' :: (a->Bool) -> [a] -> Bool
all' f xs= and' $ map' f xs

iterate' :: (a->a) -> a -> [a]
iterate' f x = let it = f x
                in x : iterate' f it

chunk' :: Int -> [a] -> [[a]]
chunk' n [] = []
chunk' n xs = let item = take' n xs
                   in item : chunk' n (drop n xs)

splitAt' :: Int -> [a] -> ([a],[a])
splitAt' n xs = (take' n xs,drop' n xs)


takeWhile' :: (a->Bool) -> [a] -> [a]
takeWhile' _ [] = []
takeWhile' f (x:xs)
    | f x = x : takeWhile' f xs
    | otherwise = []

dropWhile' :: (a->Bool) -> [a] -> [a]
dropWhile' _ [] = []
dropWhile' f (x:xs)
    | f x = dropWhile' f xs
    | otherwise = x:xs

span' :: (a->Bool) -> [a] -> ([a],[a])
span' f xs = (takeWhile' f xs,dropWhile' f xs)

break' :: (a->Bool) -> [a] -> ([a],[a])
break' f xs = span' (not'.f) xs

--wrong
groupBy' :: (a->a->Bool) -> [a] -> [[a]]
groupBy' _ [] = []
groupBy' f xs@(x:_) = let fx = f x
                          (groupItem,remainList) = span' fx xs
                      in groupItem : groupBy' f remainList

group' :: Eq a => [a] -> [[a]]
group' = groupBy' (==)

inits' :: [a] -> [[a]]
inits' xs = [] : reverse' (takeWhile' (not'.null') $ iterate' init xs)

tails' :: [a] -> [[a]]
tails' xs = (takeWhile' (not.null) $ iterate' tail xs) ++ [[]]

isInfixOf' :: Eq a => [a] -> [a] -> Bool
isInfixOf' needle haystack = let needleLen = length' needle
                                 matchList = [ take' needleLen (drop n haystack) | n<- [0..(length' haystack)-1]]
                                 in not'.null' $ takeWhile' (==needle) matchList

isPrefixOf' :: Eq a => [a] -> [a] -> Bool
isPrefixOf' needle haystack = let match = take (length needle) haystack
                                in match == needle

isSuffixOf' :: Eq a => [a] -> [a] -> Bool
isSuffixOf' needle haystack = let match = drop (max 0 ((length haystack) - (length needle))) haystack
                                 in match == needle

partition' :: (a -> Bool) -> [a] -> ([a],[a])
partition' f xs = (filter' f xs, filter' (not'.f) xs)

find' :: (a->Bool) -> [a] -> Maybe a
find' f [] = Nothing
find' f (x:xs)
    | f x = Just x
    | otherwise = find' f xs

findIndex' :: (a->Bool) -> [a] -> Maybe Int
findIndex' f xs = let items = zip [0..(length' xs)-1] xs
                      findItem = find' (\(i,a) -> f a) items
                      in if isNothing' findItem then Nothing else Just (fst' (fromJust' findItem))

findIndices' :: (a->Bool) -> [a] -> [Int]
findIndices' f xs = let items = zip [0..(length' xs)-1] xs
                        in map' fst' $ filter' (\(i,a) -> f a) items

elemIndex' :: Eq a => a -> [a] -> Maybe Int
elemIndex' x xs = findIndex' (==x) xs

elemIndices' :: Eq a => a -> [a] -> [Int]
elemIndices' x xs = findIndices' (==x) xs

zip3' :: [a] -> [b] -> [c] -> [(a,b,c)]
zip3' [] _ _  = []
zip3' (a:as) (b:bs) (c:cs) = (a,b,c) : zip3' as bs cs

-- Data.List.Split
split' :: Eq a => a -> [a] -> [[a]]
split' _ [] = []
split' delimit xs = let  (item,remainList) = break' (==delimit) xs
                         remainItems = split' delimit (drop' 1 remainList)
                         in item:remainItems

lines' :: String -> [String]
lines' = split' '\n'

unlines' :: [String] -> String
unlines' = intercalate' "\n"

isSpace' :: Char -> Bool
isSpace' ' ' = True
isSpace' _ = False

words' :: String -> [String]
{-words' "" = []
words' s = filter' (not'.null') $ split' ' ' s-}
words' = filter' (not'.any' isSpace') . groupBy' ((==) `on'` isSpace')

unwords' :: [String] -> String
unwords' = intercalate' " "

nubBy' ::(a->a->Bool) -> [a] -> [a]
nubBy' f = foldl' (\acc x ->if or' $ map' (f x) acc then acc else acc ++ [x]) []

nub' :: Eq a => [a] -> [a]
nub' = nubBy' (==)


deleteBy' :: (a->a->Bool) -> a -> [a] -> [a]
deleteBy' f x xs = let idx = findIndex' (\a -> f a x) xs
                   in if idx == Nothing then xs else take' (fromJust' idx) xs ++ drop' (1+fromJust' idx) xs

delete' :: Eq a => a -> [a] -> [a]
delete' = deleteBy' (==)

union' :: Eq a => [a] -> [a] -> [a]
union' as [] = as
union' as (b:bs)
    | b `elem` as = union' as bs
    | otherwise = b: union' as bs


intersection' :: Eq a => [a] -> [a] -> [a]
intersection' as [] = []
intersection' as (b:bs)
    | b `elem` as = b : intersection' as bs
    | otherwise = intersection' as bs

different' :: Eq a => [a] -> [a] -> [a]
different' [] bs = []
different' (a:as) bs
    | a `elem` bs = different' as bs
    | otherwise = a : different' as bs

insert' :: Ord a => a -> [a] -> [a]
insert' x [] = [x]
insert' x (a:as)
    | x < a = x:a:as
    | otherwise = a : insert' x as


-- Data.Char

-- Data.Map
findKey' :: (Eq k) => k -> [(k,v)] -> v
findKey' x xs = snd'.head'.filter' (\(k,v) -> x == k) $ xs

