@fast

Feature: Get Wordlist

  Scenario: get_word_list is used to fetch eff list
    Given: get_word_list runs
    When: eff wordlist is fetched
    Then: the first entry is '11111	abacus'
