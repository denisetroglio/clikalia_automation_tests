Feature: Mortgage offer

    Background:
        Given the user access the Clikalia webpage
        When the user start to search an apartment on Madrid


    Scenario: User make a valid mortgage offer
        Then the user select an apartment to make an offer

    Scenario: User make an invalid mortgage offer
        Given the user select an apartment to make an invalid offer