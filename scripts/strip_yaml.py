import os
import glob

def remove_yaml_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    if not lines:
        return
        
    if lines[0].strip() == '---':
        # Find the closing ---
        closing_idx = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                closing_idx = i
                break
                
        if closing_idx != -1:
            # We found a YAML block, strip it out
            new_lines = lines[closing_idx + 1:]
            
            # Optional: strip leading blank lines
            while len(new_lines) > 0 and new_lines[0].strip() == '':
                new_lines.pop(0)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Removed YAML from {filepath}")

for root, _, files in os.walk('/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo'):
    for file in files:
        if file.endswith('.md'):
            remove_yaml_frontmatter(os.path.join(root, file))
