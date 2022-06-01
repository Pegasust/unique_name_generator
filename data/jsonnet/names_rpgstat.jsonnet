// A small and simple data for generating names using existing RPG stats
{
    // The requirements for a script to run with this data
    // Each entry represents an "or"
    // If dataTags is empty, it is automatically
    // compatible with all generators
    "dataTags": [
        "linear",
        "foo",
        "bar",
        ["recursive", "match-or"], // each list-entry represents an "and"
        ["recursive", "match-and"]
    ],
    
    // The example says:
    // This data set is best used with scripts with tag:
    // linear || foo || bar || (recursive && match-or) || (recursive && match-and)
    // symbols to be used as name generation candidate
    "symbols": 
    [
        {
            "name": "hello",
            "keywords": [
                "cheerful",
                "greetings",
                "positive",
                "beginning"
            ]
        },
        {
            "name": "world",
            "keywords": [
                "huge",
                "location",
                "life"
            ]
        }
    ]
}