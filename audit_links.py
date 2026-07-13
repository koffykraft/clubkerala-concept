#!/usr/bin/env python3
import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

def extract_links(html_content, file_path):
    """Extract all href and src attributes from HTML"""
    links = []
    
    # Find all href links
    href_pattern = r'href=["\']([^"\']+)["\']'
    hrefs = re.findall(href_pattern, html_content)
    links.extend([(link, 'href') for link in hrefs])
    
    # Find all src links (images, scripts)
    src_pattern = r'src=["\']([^"\']+)["\']'
    srcs = re.findall(src_pattern, html_content)
    links.extend([(link, 'src') for link in srcs])
    
    return links

def check_link(link, base_path, root_dir):
    """Check if a link is valid"""
    # Skip external links
    if link.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
        return True, "external or anchor"
    
    # Skip just hash
    if link == '#':
        return True, "anchor"
    
    # Remove hash fragments
    link_without_hash = link.split('#')[0]
    if not link_without_hash:
        return True, "anchor only"
    
    # Resolve relative path
    if link_without_hash.startswith('/'):
        full_path = root_dir / link_without_hash.lstrip('/')
    else:
        full_path = (base_path.parent / link_without_hash).resolve()
    
    # Check if file exists
    exists = full_path.exists()
    return exists, str(full_path) if not exists else "ok"

def audit_site(root_dir):
    """Audit all HTML files in the site"""
    root_path = Path(root_dir)
    html_files = list(root_path.rglob('*.html'))
    
    broken_links = []
    total_links = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = extract_links(content, html_file)
            
            for link, link_type in links:
                total_links += 1
                is_valid, reason = check_link(link, html_file, root_path)
                
                if not is_valid:
                    broken_links.append({
                        'file': str(html_file.relative_to(root_path)),
                        'link': link,
                        'type': link_type,
                        'reason': reason
                    })
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    
    return broken_links, total_links, len(html_files)

if __name__ == '__main__':
    root_dir = '/app/KOFFYKRAFT-main'
    
    print("=== KOFFYKRAFT LINK AUDIT ===\n")
    broken, total, files = audit_site(root_dir)
    
    print(f"Files scanned: {files}")
    print(f"Total links found: {total}")
    print(f"Broken links: {len(broken)}\n")
    
    if broken:
        print("=== BROKEN LINKS ===\n")
        for item in broken[:50]:  # Show first 50
            print(f"File: {item['file']}")
            print(f"  Link: {item['link']} ({item['type']})")
            print(f"  Issue: {item['reason']}")
            print()
        
        if len(broken) > 50:
            print(f"\n... and {len(broken) - 50} more broken links")
    else:
        print("✓ No broken links found!")
