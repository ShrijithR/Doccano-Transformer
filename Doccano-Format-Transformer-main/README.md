# DoccanoFormatTransformer
A converter program for changing doccano export format pattern to required output format

## What's the problem?  
Current version of Doccano in Azure doesn't export the labelled dataset according to the required format to train Spacy model.  

## Instructions
1. Open cmd.
2. Run the application 'transformer.py' file with the arguments according to the following syntax:  
    application-name filename/filepath label-keys:label-names, ...

### Syntax rules
1. The entirety of the label keys and names shall not be separated by space/symbols other than colon or comma. 
2. The dataset file format must be included.  
    Example: transformer.py test_dataset.jsonl 7:generic,8:skills,9:mandatory
3. The output file is exported in the same folder and uses 'corrected_' before the original filename.   

### Current export format
```
{"id": 1893, 
"text": "Fluency in Hindi/Marathi language is compulsary.Must have knowl.Bilingual Marathi,Spanish is preferred.", 
"annotations": \[{"label": 8, "start_offset": 2766, "end_offset": 2773, 
"user": 1, "created_at": "2021-04-09T06:35:39.010628Z", "updated_at": "2021-04-09T06:35:39.010659Z"}, 
{"label": 8, "start_offset": 2758, "end_offset": 2765, 
"user": 1, "created_at": "2021-04-09T06:35:39.008555Z", "updated_at": "2021-04-09T06:35:39.008568Z"}], 
"meta": {}, "annotation_approver": null, "comment_count": 0}
```

### Required format
```
("Fluency in Hindi/Marathi language is compulsary.Must have knowl.Bilingual Marathi,Spanish is preferred.", 
{"entities": \[2766, 2773, "generic"], \[2758, 2765, "generic"]]
}), 
```

| Current format | Required format
| --- | --- |
| `{"id": 1893, "text": "Fluency...` | `("Fluency...`
| `"annotations": \[{"label"` | `{"entities":\[\[...`
| `\[{"label": 8, "start_offset": 2766, "end_offset": 2773, "user": 1, "created_at": "2021-04-09T06:35:39.010628Z", "updated_at": "2021-04-09T06:35:39.010659Z"},` | `\[\[2766, 2773, "generic"], \[34, ...] ]`
| `...\], "meta": {}, "annotation_approver": null, "comment_count": 0}` | `]}),`
