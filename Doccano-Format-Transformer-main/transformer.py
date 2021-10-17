import re, sys, os

class Transformer:
    def __init__(self, filename: str, label_details: dict[int, str]):
        self.file_name = filename
        self.label_id = label_details.keys()
        self.label_name = label_details.values()

        with open(self.file_name) as file_input:
            self.replaced_text = file_input.read()

        self.associated_text = {
            r', "user": [0-9]*, '
            r'"created_at": "2021-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*Z", '
            r'"updated_at": "2021-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*Z"\}(,)?': 
            '',
            r', "meta": \{\}, "annotation_approver": [a-z]*, "comment_count": [0-9]}':
            '}),',
            r'"annotations"': 
            '{"entities"',
            r'"text": ': 
            '(',
            r'annotations':
            'entities',
            r'{"id": [0-9]*, ': 
            '',
        }

    def replace_text(self):        
        for id, name in zip(self.label_id, self.label_name):
            self.replaced_text = re.sub(
                '{' + r'"label": {0}, "start_offset": ([0-9]*), "end_offset": ([0-9]*)'.format(id), 
                fr'[\g<1>, \g<2>, "{name}"],', 
                self.replaced_text
                )
        for replace_this, replace_by_this in self.associated_text.items():
            self.replaced_text = re.sub(replace_this, replace_by_this, self.replaced_text)    

        with open('corrected_'+self.file_name, 'w') as file_output:
            file_output.write(self.replaced_text)        

def input_extraction():
    try:
        file_name = sys.argv[1]
        user_input_label = sys.argv[2]
    except IndexError:
        sys.exit('Enter input in proper format')
    assert os.path.exists(file_name), "Enter proper filename (Along with path if necessary)"
    file_name = os.path.basename(file_name)

    re_input_label = re.compile('(\d{0,2}):([A-Za-z]*)')
    label_list = re_input_label.findall(user_input_label) 
    assert label_list != None, "The labels shouldn't be empty"
    
    label_dict = {}
    for e in label_list:
        label_dict[int(e[0])] = e[-1]

    return file_name, label_dict

if __name__ == "__main__":
    file_name, label_dict = input_extraction()
    transform = Transformer(file_name, label_dict)
    transform.replace_text()
