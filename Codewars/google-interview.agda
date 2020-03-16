{-# OPTIONS --safe #-}
module FlipTreeSym where

open import Relation.Binary.PropositionalEquality
open import Preloaded

{-
Preloaded:

module Preloaded where

data Tree (A : Set) : Set where
  leaf : A → Tree A
  branch : A → Tree A → Tree A → Tree A

flipTree : {A : Set} → Tree A → Tree A
flipTree (leaf x) = leaf x
flipTree (branch x l r) = branch x (flipTree r) (flipTree l)
-}

flipTreeSym : {A : Set} → (t : Tree A) → t ≡ flipTree (flipTree t)
flipTreeSym (leaf x) = refl
flipTreeSym (branch x l r) rewrite sym (flipTreeSym l) | sym (flipTreeSym r) = refl



{- Naive version

module FlipTreeSym where
{-
open import Relation.Binary.PropositionalEquality
-}
open import Preloaded
import Relation.Binary.PropositionalEquality as Eq
open Eq using (_≡_; refl; cong; sym)
open Eq.≡-Reasoning
  using (begin_; _≡⟨⟩_; _≡⟨_⟩_;  _∎)


{-
Preloaded:

module Preloaded where

data Tree (A : Set) : Set where
  leaf : A → Tree A
  branch : A → Tree A → Tree A → Tree A

flipTree : {A : Set} → Tree A → Tree A
flipTree (leaf x) = leaf x
flipTree (branch x l r) = branch x (flipTree r) (flipTree l)
-}


flipTreeSym : {A : Set} → (t : Tree A) → t ≡ flipTree (flipTree t) 
flipTreeSym (leaf x) = refl
flipTreeSym (branch x l r) = 
  begin
    branch x l r
  ≡⟨ cong (branch x l) (flipTreeSym r) ⟩
    branch x l (flipTree (flipTree r))
  ≡⟨ cong (\l' → branch x l' (flipTree (flipTree r))) (flipTreeSym l) ⟩
    branch x (flipTree (flipTree l)) (flipTree (flipTree r))
  ≡⟨⟩
    flipTree (branch x (flipTree r) (flipTree l))
  ≡⟨⟩
    flipTree (flipTree (branch x l r))
  ∎


-}

