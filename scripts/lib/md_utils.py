"""Markdown utilities for Web Platform knowledgebase documents."""
import os
import re

def compress_markdown(content: str) -> str:
    """Strip comments, trailing spaces, and collapse duplicate blank lines."""
    # 1. Strip redundant HTML comments <!-- ... -->
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # 2. Strip trailing whitespaces on each line
    lines = [line.rstrip() for line in content.splitlines()]
    
    # 3. Collapse multiple consecutive blank lines into a single blank line
    compressed_lines = []
    prev_blank = False
    for line in lines:
        is_blank = (len(line) == 0)
        if is_blank:
            if not prev_blank:
                compressed_lines.append(line)
                prev_blank = True
        else:
            compressed_lines.append(line)
            prev_blank = False
            
    return "\n".join(compressed_lines) + "\n"

def strip_yaml_frontmatter(content: str) -> str:
    """Remove YAML frontmatter metadata block at the top of markdown content."""
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != '---':
        return content
        
    closing_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            closing_idx = i
            break
            
    if closing_idx != -1:
        new_lines = lines[closing_idx + 1:]
        while len(new_lines) > 0 and new_lines[0].strip() == '':
            new_lines.pop(0)
        return "".join(new_lines)
    return content

def process_markdown_directory(root_dir: str, compress: bool = True, remove_yaml: bool = False):
    """Process all markdown files under root_dir."""
    total_files = 0
    orig_bytes = 0
    comp_bytes = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ('venv', '.venv', 'node_modules')]
        
        for fname in filenames:
            if fname.endswith('.md'):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        original = f.read()
                    
                    text = original
                    if remove_yaml:
                        text = strip_yaml_frontmatter(text)
                    if compress:
                        text = compress_markdown(text)
                    
                    o_size = len(original.encode('utf-8'))
                    c_size = len(text.encode('utf-8'))
                    
                    if original != text:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(text)
                        total_files += 1
                        orig_bytes += o_size
                        comp_bytes += c_size
                except Exception as e:
                    print(f"Error processing {fpath}: {e}")
                    
    saved_bytes = orig_bytes - comp_bytes
    est_tokens = saved_bytes // 4
    print(f"Finished processing {total_files} Markdown files.")
    print(f"Original Size: {orig_bytes} bytes | Processed Size: {comp_bytes} bytes")
    print(f"Saved: {saved_bytes} bytes (~{est_tokens} tokens saved).")
