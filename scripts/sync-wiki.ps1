param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")),
    [string]$WikiClonePath = (Join-Path (Split-Path (Resolve-Path (Join-Path $PSScriptRoot "..")) -Parent) "dio-estudos-logica-python-wiki-sync")
)

$ErrorActionPreference = "Stop"

$wikiRemote = "https://github.com/matheusflorindo32/dio-estudos-logica-python.wiki.git"
$sourcePath = Join-Path $RepositoryRoot "wiki"
$pages = @(
    "Home.md",
    "Introducao-a-Logica-de-Programacao-com-Python.md",
    "Estruturas-Condicionais.md",
    "Estruturas-de-Repeticao.md",
    "Funcoes-em-Python.md"
)

if (-not (Test-Path $sourcePath)) {
    throw "Pasta de origem não encontrada: $sourcePath"
}

foreach ($page in $pages) {
    $sourceFile = Join-Path $sourcePath $page
    if (-not (Test-Path $sourceFile)) {
        throw "Página de origem ausente: $sourceFile"
    }
}

if (Test-Path $WikiClonePath) {
    $gitDir = Join-Path $WikiClonePath ".git"
    if (-not (Test-Path $gitDir)) {
        throw "O destino já existe e não é um clone Git: $WikiClonePath"
    }

    Push-Location $WikiClonePath
    try {
        if (git status --porcelain) {
            throw "O clone da Wiki possui alterações locais. Preserve-as antes de sincronizar."
        }
        git pull --ff-only
    }
    finally {
        Pop-Location
    }
}
else {
    git clone $wikiRemote $WikiClonePath
}

foreach ($page in $pages) {
    Copy-Item (Join-Path $sourcePath $page) (Join-Path $WikiClonePath $page) -Force
}

Push-Location $WikiClonePath
try {
    git diff --check
    git status --short

    if (-not (git status --porcelain)) {
        Write-Host "A Wiki oficial já está sincronizada."
        exit 0
    }

    git add -- $pages
    git commit -m "docs: publica experiencia visual e didatica da Wiki"
    git push origin (git branch --show-current)
    Write-Host "Wiki oficial sincronizada com sucesso."
}
finally {
    Pop-Location
}
