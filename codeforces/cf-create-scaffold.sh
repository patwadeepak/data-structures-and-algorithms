#!/bin/bash

# Check if we're in the codeforces directory or navigate to it
current_dir=$(basename "$PWD")
if [ "$current_dir" != "codeforces" ]; then
    if [ -d "codeforces" ]; then
        echo "Not in codeforces directory. Changing to codeforces directory..."
        cd codeforces
    else
        echo "Error: Not in codeforces directory and no codeforces folder found in current directory."
        echo "Please run this script from the codeforces directory or from a directory containing a codeforces folder."
        exit 1
    fi
fi

# Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Codeforces Contest/Practice Scaffold Creator${NC}"
echo "============================================="

# Ask if it's a contest or practice
echo -e "\n${YELLOW}Are you participating in a contest or is it practice?${NC}"
echo "1) Contest (contests-participated)"
echo "2) Practice (practice)"
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        folder_type="contests-participated"
        echo -e "${GREEN}Selected: Contest${NC}"
        ;;
    2)
        folder_type="practice"
        echo -e "${GREEN}Selected: Practice${NC}"
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

# Ask for contest name
echo -e "\n${YELLOW}Enter the contest name:${NC}"
echo "Example: Codeforces Round 1044 (Div. 2)"
read -p "Contest name: " contest_name

if [ -z "$contest_name" ]; then
    echo -e "${RED}Contest name cannot be empty. Exiting.${NC}"
    exit 1
fi

# Ask for problem names
echo -e "\n${YELLOW}Enter the problem names separated by spaces:${NC}"
echo "Example: A B C1 C2 D E F1 F2 F3"
echo "or: A B C D E F"
read -p "Problem names: " problems

if [ -z "$problems" ]; then
    echo -e "${RED}Problem names cannot be empty. Exiting.${NC}"
    exit 1
fi

# Create the contest folder
contest_path="$folder_type/$contest_name"
echo -e "\n${BLUE}Creating contest folder: $contest_path${NC}"

if [ -d "$contest_path" ]; then
    echo -e "${YELLOW}Warning: Folder already exists. Files will be added/overwritten.${NC}"
else
    mkdir -p "$contest_path"
fi

# Create files for each problem
echo -e "\n${BLUE}Creating files for problems...${NC}"

for problem in $problems; do
    echo -e "${GREEN}Creating files for problem: $problem${NC}"
    
    # Create Python file with template
    cat > "$contest_path/$problem.py" << EOF
def solve(a, n):
    pass


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
EOF

    # Create empty input file
    touch "$contest_path/$problem.in"
    
    # Create empty output files
    touch "$contest_path/$problem.outputCorrect"
    touch "$contest_path/$problem.outputSolved"
    
    echo "  ✓ $problem.py"
    echo "  ✓ $problem.in"
    echo "  ✓ $problem.outputCorrect"
    echo "  ✓ $problem.outputSolved"
done

echo -e "\n${GREEN}✅ Contest scaffold created successfully!${NC}"
echo -e "${BLUE}📁 Location: $contest_path${NC}"
echo -e "${BLUE}📝 Problems: $problems${NC}"