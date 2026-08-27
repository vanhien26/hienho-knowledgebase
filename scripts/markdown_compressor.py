#!/usr/bin/env python3
import os
import re
import sys

def compress_markdown(content):
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
            
    result = "\n".join(compressed_lines) + "\n"
    return result

def process_directory(root_dir):
    total_files = 0
    orig_bytes = 0
    comp_bytes = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude hidden dirs & virtualenvs
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ('venv', '.venv', 'node_modules')]
        
        for fname in filenames:
            if fname.endswith('.md'):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        original = f.read()
                    
                    compressed = compress_markdown(original)
                    
                    o_size = len(original.encode('utf-8'))
                    c_size = len(compressed.encode('utf-8'))
                    
                    if original != compressed:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(compressed)
                        total_files += 1
                        orig_bytes += o_size
                        comp_bytes += c_size
                except Exception as e:
                    print(f"Error processing {fpath}: {e}")
                    
    saved_bytes = orig_bytes - comp_bytes
    est_tokens = saved_bytes // 4
    print(f"✅ Finished compressing {total_files} Markdown files.")
    print(f"📊 Original Size: {orig_bytes} bytes")
    print(f"📊 Compressed Size: {comp_bytes} bytes")
    print(f"⚡ Saved: {saved_bytes} bytes (~{est_tokens} tokens saved).")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    process_directory(target)
