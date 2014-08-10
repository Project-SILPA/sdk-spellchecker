Usage
=====

### To check correctness of a word 

```
        SpellChecker spellChecker = new SpellChecker(getContext());
        boolean isCorrect1 = spellChecker.check("Judicious");
        // isCorrect1 <- true;
        boolean isCorrect2 = spellChecker.check("Judecious");
        // isCorrect2 <- false;

```

The above function `check(String)` returns true if word is spelt correctly else false.


### To get suggestions

```
        SpellChecker spellChecker = new SpellChecker(getContext());
        String suggestedWords = spellChecker.suggest("ext", null, 2);
        // suggestedWords <- [east, exact, exist, exit]

```

The above function `suggest(String, String, int)` returns suggestions of words. Function signatures are :

```
        public List<String> suggest(String word); 
        public List<String> suggest(String word, String language);
        public List<String> suggest(String word, String language, int distance);

```

Arguments :

```
        word - word for which  spelling suggestions are required.
        language - language of word. Default value - null in which case language is auto detected.
        distance - suggestion will contain words with length = word length +/-  distance. Default value - 2

```

### To check batch of words 

```
        SpellChecker spellChecker = new SpellChecker(getContext());
        List<String> mispeltWords = spellChecker.checkBatch("The queck bron foox jumps ower the lazzy dog")
        // mispeltWords <- [queck, bron, foox, ower, lazzy]

```

The above function `check(String)` returns true if word is spelt correctly else false.


#### To run tests
Tests present at `/src/androidTest/java/org/silpa/spellchecker/TestSpellChecker.java`

  - Select test to run
  - Right Click -> Run Test -> Run as Android Test

