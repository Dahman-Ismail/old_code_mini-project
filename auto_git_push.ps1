# === auto_git_push.ps1 ===
# Path to your local git repo
$repoPath = "C:\Users\Sanae\Desktop\tesssst\python"

# Commit message (you can include date)
# $commitMessage = "Auto commit on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$commitMessage = " commit onchange"

# Go to repo folder
Set-Location $repoPath

# Add all changes
git add .

# Commit (ignore if nothing changed)
git commit -m $commitMessage --allow-empty

# Push to main branch
git push -u origin main
