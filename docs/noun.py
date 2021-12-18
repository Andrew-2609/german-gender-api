get_all_nouns_responses = {
    200: {
        "description": "Return a pageable collection of available Nouns in the database,"
                       " excluding Nouns with the gender to be defined.",
        "content": {
            "application/json": {
                "example": {
                    "content": [
                        {
                            "noun": "Abberufung",
                            "gender": "feminine",
                            "articles": {
                                "nominative": "die",
                                "accusative": "die",
                                "dative": "den",
                                "genitive": "der"
                            }
                        },
                        {
                            "noun": "Abbestellung",
                            "gender": "feminine",
                            "articles": {
                                "nominative": "die",
                                "accusative": "die",
                                "dative": "den",
                                "genitive": "der"
                            }
                        }
                    ],
                    "page": 10,
                    "size": 2
                }
            }
        },
    },
    422: {
        "description": "Some of the query params is invalid. Probably, it is 'gender', which can only be:"
                       " masculine, feminine, neuter or tbd (to be defined).",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": [
                                "query",
                                "gender"
                            ],
                            "msg": "value is not a valid enumeration member; permitted: "
                                   "'masculine', 'feminine', 'neuter', 'tbd'",
                            "type": "type_error.enum",
                            "ctx": {
                                "enum_values": [
                                    "masculine",
                                    "feminine",
                                    "neuter",
                                    "tbd"
                                ]
                            }
                        }
                    ]
                }
            }
        },
    }
}

get_noun_responses = {
    200: {
        "description": "Return the searched Noun informations.",
        "content": {
            "application/json": {
                "example": {
                    "noun": "Mädchen",
                    "gender": "neuter",
                    "articles": {
                        "nominative": "das",
                        "accusative": "das",
                        "dative": "dem",
                        "genitive": "des"
                    }
                }
            }
        }
    },
    404: {
        "description": "The searched Noun does not exist in the database.",
        "content": {
            "application/json": {
                "example": {
                    "detail": {
                        "message": "Noun 'Hund' was not found",
                        "procedure": "If you are sure that it sould exist, please contact me at "
                                     "andrew.agoravai@gmail.com",
                        "url": "/api/v1/nouns/Hund"
                    }
                }
            }
        }
    },
    422: {
        "description": "This is shown by FastAPI by default, but it does not occur in this case =)."
    }
}
