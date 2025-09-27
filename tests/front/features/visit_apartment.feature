Feature: Visit Clikalia webpage

    Scenario: User visits an apartment in Madrid

        Given the user access the Clikalia webpage
        When the user start to search a apartment on Madrid
        Then the user select a apartment
        Given the client schedules a visit


