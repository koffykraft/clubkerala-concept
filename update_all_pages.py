#!/usr/bin/env python3
"""
Script to update all HTML files to use the new minimal.css stylesheet
and add consistent navigation
"""

import os
import re
from pathlib import Path

def get_css_path(file_path, root_dir):
    """Calculate relative path to minimal.css from any file"""
    relative_path = file_path.relative_to(root_dir)
    depth = len(relative_path.parents) - 1
    return '../' * depth + 'assets/site/minimal.css'

def get_home_path(file_path, root_dir):
    """Calculate relative path to home from any file"""
    relative_path = file_path.relative_to(root_dir)
    depth = len(relative_path.parents) - 1
    return '../' * depth if depth > 0 else './'

def update_html_file(file_path, root_dir):
    """Update a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already using minimal.css
        if 'minimal.css' in content:
            return False, "Already updated"
        
        # Calculate paths
        css_path = get_css_path(file_path, root_dir)
        home_path = get_home_path(file_path, root_dir)
        
        # Replace old CSS references
        content = re.sub(
            r'<link rel="stylesheet" href="[^"]*passage\.css">',
            f'<link rel="stylesheet" href="{css_path}">',
            content
        )
        
        content = re.sub(
            r'<link rel="stylesheet" href="[^"]*styles\.css">',
            f'<link rel="stylesheet" href="{css_path}">',
            content
        )
        
        # Remove inline <style> tags (but preserve content for manual review)
        if '<style>' in content and 'training/' in str(file_path):
            # Replace inline styles with external CSS link
            content = re.sub(
                r'<style>.*?</style>',
                f'<link rel="stylesheet" href="{css_path}">',
                content,
                flags=re.DOTALL
            )
        
        # Add mobile menu toggle script if not present
        if 'function toggleMenu()' not in content and '</body>' in content:
            menu_script = '''
  <script>
    function toggleMenu() {
      document.getElementById('mainNav').classList.toggle('active');
    }
  </script>
</body>'''
            content = content.replace('</body>', menu_script)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Updated"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    root_dir = Path('/app/KOFFYKRAFT-main')
    
    # Find all HTML files
    html_files = list(root_dir.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files\n")
    
    updated = 0
    skipped = 0
    errors = 0
    
    for html_file in html_files:
        # Skip catalog files and samples
        if 'catalog' in html_file.name or 'sample' in html_file.name:
            continue
        
        success, message = update_html_file(html_file, root_dir)
        
        relative_path = html_file.relative_to(root_dir)
        
        if success:
            updated += 1
            print(f"✓ {relative_path}")
        elif "Already updated" in message:
            skipped += 1
        else:
            errors += 1
            print(f"✗ {relative_path}: {message}")
    
    print(f"\n=== Summary ===")
    print(f"Updated: {updated}")
    print(f"Skipped (already updated): {skipped}")
    print(f"Errors: {errors}")
    print(f"Total: {len(html_files)}")

if __name__ == '__main__':
    main()
