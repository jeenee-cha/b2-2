# Troubleshooting Log

이 문서는 실제로 실행한 Git 복구 명령을 재현 가능하게 남기는 기록지입니다. 명령을 실행하기 전에 현재 브랜치와 push 여부를 확인하고, 실행 직후 터미널 출력과 commit/PR URL을 해당 자리표시자에 붙여 넣습니다.

## 안전 원칙

- `amend`와 `reset --soft`는 push 전 김씨 개인 브랜치에서만 실행합니다.
- 이미 원격과 `main`에 공유된 변경은 차씨가 별도 브랜치에서 `revert`합니다.
- `reset --hard`, `push --force`, 공유 브랜치 rebase는 사용하지 않습니다.
- 각 시나리오는 실행자 외 팀원 1명이 명령과 결과를 확인합니다.

---

## 시나리오 1 · 최근 로컬 커밋 메시지 수정 (`git commit --amend`)

### 참여자와 위치

- 실행·기록: 김씨
- 확인: 송씨
- 브랜치: `feature/kim-conflict-troubleshooting`
- 관련 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/12` / `https://github.com/jeenee-cha/b2-2/pull/15`

### 상황

김씨가 README 충돌용 문장을 수정한 뒤 최근 커밋 메시지를 의도적으로 `docs: update`라고 작성합니다. 이 메시지는 과제의 금지 예시이므로 원격에 push하기 전에 구체적으로 고칩니다.

### 실행 명령

```bash
git status
git add README.md
git commit -m "docs: update"
git log --oneline -1
git branch -r --contains HEAD
git commit --amend -m "docs: 김씨 버전 프로젝트 설명 준비"
git log --oneline -2
```

`git branch -r --contains HEAD`는 해당 commit이 아직 원격에 없는지 확인하는 명령입니다. amend 후 메시지는 `docs/CONTRIBUTING.md` 3절의 `<영문 type>: <한글 설명>` 형식을 따릅니다.

`git log` 두 번의 출력을 복사한 뒤에만 push합니다.

```bash
git push -u origin feature/kim-conflict-troubleshooting
```

### 실제 결과(김씨 작성)

- 실행 날짜: `2026-09-30`
- amend 전 hash·메시지: `4ece798 docs: update`
- amend 후 hash·메시지: `e5d3953 docs: 김씨 버전 프로젝트 설명 준비`
- push 전 원격 포함 여부: `git branch -r --contains HEAD` 출력 없음
- 원격에 올라간 commit: `e5d3953`만 존재하며 `docs: update`는 push되지 않음

실제 터미널 출력:

```text
$ git commit -m "docs: update"
[feature/kim-conflict-troubleshooting 4ece798] docs: update
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git log --oneline -1
4ece798 docs: update
$ git branch -r --contains HEAD
$ git commit --amend -m "docs: 김씨 버전 프로젝트 설명 준비"
[feature/kim-conflict-troubleshooting e5d3953] docs: 김씨 버전 프로젝트 설명 준비
 Date: Wed Sep 30 15:35:00 2026 +0900
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git log --oneline -2
e5d3953 docs: 김씨 버전 프로젝트 설명 준비
82df3ef Merge pull request #10 from jeenee-cha/feature/song-string-utils
$ git reflog -3
e5d3953 HEAD@{0}: commit (amend): docs: 김씨 버전 프로젝트 설명 준비
4ece798 HEAD@{1}: commit: docs: update
82df3ef HEAD@{2}: checkout: moving from main to feature/kim-conflict-troubleshooting
```

- hash가 바뀐 이유: 커밋 객체의 메시지가 바뀌어 새 커밋으로 다시 만들어졌기 때문입니다.
- 확인자 송씨의 확인 내용: `https://github.com/jeenee-cha/b2-2/pull/15#issuecomment-5906852904` (원격에 `e5d3953`만 있고 `4ece798 docs: update`는 없음을 확인)

### 선택 이유와 주의점

최근 로컬 커밋 하나의 메시지만 고치는 상황이므로 amend가 적절합니다. 이미 push한 커밋에 amend를 사용하면 원격과 다른 히스토리가 되어 force push가 필요할 수 있으므로 이번 실습에서는 금지합니다.

---

## 시나리오 2 · 커밋 취소 후 변경 유지 (`git reset --soft HEAD~1`)

### 참여자와 위치

- 실행·기록: 김씨
- 확인: 차씨
- 브랜치: `feature/kim-conflict-troubleshooting`
- 관련 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/12` / `https://github.com/jeenee-cha/b2-2/pull/15`

### 상황

김씨가 amend 기록을 문서에 적다가 설명이 부족한 상태로 커밋했습니다. 아직 push하지 않았고 파일 변경을 잃지 않은 채 커밋만 취소하여 보완하려고 합니다.

### 실행 명령

```bash
# VS Code에서 이 시나리오의 실제 결과 초안을 작성
git add docs/troubleshooting-log.md
git commit -m "docs: 소프트 리셋 실습 기록 초안"
git log --oneline -2
git branch -r --contains HEAD
git reset --soft HEAD~1
git status
# 설명과 실제 출력을 보완
git add docs/troubleshooting-log.md
git commit -m "docs: amend 및 soft reset 실습 기록"
git log --oneline -2
```

모든 명령 결과를 확인합니다. 이 commit은 I5를 merge하여 README 충돌을 해결한 commit과 함께 push합니다.

```bash
git fetch origin
git merge origin/main
# README 충돌 해결과 conflict-resolution 기록 후 commit
git push
```

### 실제 결과(김씨 작성)

- 실행 날짜: `2026-09-30`
- reset으로 취소한 커밋 hash: `cda3d7b docs: 소프트 리셋 실습 기록 초안`
- reset 전 원격 포함 여부: `git branch -r --contains HEAD` 출력 없음
- reset 후 HEAD: `e5d3953 docs: 김씨 버전 프로젝트 설명 준비`
- reset 직후 `git status`: `Changes to be committed: modified: docs/troubleshooting-log.md`
- 변경이 보존된 파일: `docs/troubleshooting-log.md` (시나리오 1 실제 결과 34줄 추가분이 staged 상태로 유지)
- 다시 작성한 커밋 URL: `https://github.com/jeenee-cha/b2-2/commit/51797dc28ff312a9d3879fabf7963307452e8188`

실제 터미널 출력:

```text
$ git commit -m "docs: 소프트 리셋 실습 기록 초안"
[feature/kim-conflict-troubleshooting cda3d7b] docs: 소프트 리셋 실습 기록 초안
 1 file changed, 34 insertions(+), 6 deletions(-)
$ git log --oneline -2
cda3d7b docs: 소프트 리셋 실습 기록 초안
e5d3953 docs: 김씨 버전 프로젝트 설명 준비
$ git branch -r --contains HEAD
$ git reset --soft HEAD~1
$ git status
On branch feature/kim-conflict-troubleshooting
Your branch is up to date with 'origin/feature/kim-conflict-troubleshooting'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   docs/troubleshooting-log.md

$ git log --oneline -1
e5d3953 docs: 김씨 버전 프로젝트 설명 준비
$ git reflog -2
e5d3953 HEAD@{0}: reset: moving to HEAD~1
cda3d7b HEAD@{1}: commit: docs: 소프트 리셋 실습 기록 초안
```

`cda3d7b`는 push 전에 취소되어 원격에 존재하지 않습니다.
- 확인자 차씨의 리뷰 URL: `https://github.com/jeenee-cha/b2-2/pull/15#pullrequestreview-5362806386`

### 선택 이유와 주의점

커밋만 취소하고 변경을 staging area에 유지해야 하므로 `--soft`를 사용합니다. 이미 push한 커밋이나 공유 `main`에는 reset을 사용하지 않고 revert를 선택합니다.

---

## 시나리오 3 · 작업 임시 보관과 복원 (`git stash` / `git stash pop`)

### 참여자와 위치

- 실행·기록: 송씨
- 확인: 김씨
- 브랜치: `feature/song-conflict-troubleshooting`
- 관련 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/11` / `https://github.com/jeenee-cha/b2-2/pull/16`

### 상황

송씨가 작업 중 `README.md`에 임시 메모 한 줄을 추가했지만 아직 커밋할 내용은 아닙니다. 최신 `main`을 확인하기 위해 작업을 보관하고 브랜치를 전환한 뒤 다시 복원합니다.

### 실행 명령

먼저 VS Code에서 README에 `stash practice in progress`라는 임시 한 줄을 추가하되 stage하거나 commit하지 않습니다.

```bash
git status
git stash push -m "song: stash temporary README note"
git stash list
git switch main
git pull --ff-only origin main
git switch feature/song-conflict-troubleshooting
git stash pop
git status
```

복원된 임시 한 줄과 다른 작업이 모두 있는지 확인한 뒤, 임시 한 줄만 삭제합니다. rename/modify 충돌 해결 전까지 기존 커밋은 그대로 유지합니다.

### 실제 결과(송씨 작성)

- 실행 날짜: `2026-09-30`
- stash 전 `git status`: `README.md`만 `Changes not staged for commit`의 `modified`로 표시
- `git stash list`: `stash@{0}: On feature/song-conflict-troubleshooting: song: stash temporary README note`
- `stash pop` 출력: `README.md`가 다시 `modified`로 복원되고 `Dropped refs/stash@{0} (9d3a57f85a7d8f066a87d376a3da004cf5a12e83)` 표시
- pop 후 복원 파일과 충돌 여부: `README.md` 끝의 `stash practice in progress` 한 줄만 복원, 충돌 없음. 보관 중 `main`은 `82df3ef..ae9ee58`로 fast-forward되었지만 feature 브랜치의 기존 커밋 `e251744`는 그대로 유지
- 임시 한 줄 제거 확인: 해당 줄 삭제 후 `git status --short`와 `git diff --stat` 출력 없음
- 확인자 김씨의 리뷰 URL: `https://github.com/jeenee-cha/b2-2/pull/16#pullrequestreview-5363028460`

실제 터미널 출력:

```text
$ git status
On branch feature/song-conflict-troubleshooting
Your branch is up to date with 'origin/feature/song-conflict-troubleshooting'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

$ git stash push -m "song: stash temporary README note"
Saved working directory and index state On feature/song-conflict-troubleshooting: song: stash temporary README note

$ git stash list
stash@{0}: On feature/song-conflict-troubleshooting: song: stash temporary README note

$ git switch main
Switched to branch 'main'
Your branch is behind 'origin/main' by 9 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

$ git pull --ff-only origin main
From https://github.com/jeenee-cha/b2-2
 * branch            main       -> FETCH_HEAD
Updating 82df3ef..ae9ee58
Fast-forward
 README.md                                         |  2 +-
 SUBMISSION.md                                     | 30 ++++----
 docs/conflict-resolution.md                       | 60 ++++++++++++---
 docs/{conflict-demo.md => merge-conflict-demo.md} |  2 +-
 docs/troubleshooting-log.md                       | 91 +++++++++++++++++++----
 5 files changed, 140 insertions(+), 45 deletions(-)
 rename docs/{conflict-demo.md => merge-conflict-demo.md} (72%)

$ git switch feature/song-conflict-troubleshooting
Switched to branch 'feature/song-conflict-troubleshooting'
Your branch is up to date with 'origin/feature/song-conflict-troubleshooting'.

$ git stash pop
On branch feature/song-conflict-troubleshooting
Your branch is up to date with 'origin/feature/song-conflict-troubleshooting'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (9d3a57f85a7d8f066a87d376a3da004cf5a12e83)

$ git status
On branch feature/song-conflict-troubleshooting
Your branch is up to date with 'origin/feature/song-conflict-troubleshooting'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

$ git diff
diff --git a/README.md b/README.md
index d6496b4..46f1a35 100644
--- a/README.md
+++ b/README.md
@@ -79,3 +79,4 @@ b2-2/
 - [ ] `amend`, `reset --soft`, `revert`, `stash/pop`을 실제로 실행하고 기록
 - [ ] Branch Protection 설정과 `git log --oneline --graph --all` 증빙 확보
 - [ ] `SUBMISSION.md`의 모든 자리표시자를 실제 링크로 교체
+stash practice in progress

# README.md 끝의 임시 한 줄만 삭제
$ git status --short
$ git diff --stat
```

마지막 두 명령은 모두 출력이 없어, 임시 한 줄만 제거되고 다른 변경은 남지 않았음을 확인했습니다.

### 선택 이유와 주의점

완료되지 않은 변경을 의미 없는 커밋으로 남기지 않고 안전하게 브랜치를 전환하기 위해 stash를 사용합니다. `stash pop`도 충돌할 수 있으므로 반드시 출력과 `git status`를 확인합니다.

---

## 시나리오 4 · 원격과 main에 공유된 커밋 취소 (`git revert`)

### 참여자와 위치

- 실행·기록: 차씨
- 확인·리뷰: 송씨
- 대상 PR: I8 `feature/cha-revert-seed`
- revert PR: I9 `feature/cha-revert-and-submission`

### 1단계 · 되돌릴 커밋을 PR로 공유

차씨가 I8 Issue를 만든 뒤 최신 `main`에서 임시 파일을 만듭니다.

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/cha-revert-seed
# VS Code에서 docs/revert-practice.md를 만들고 임시 설명 한 줄 작성
git add docs/revert-practice.md
git commit -m "docs: add temporary revert practice note"
git push -u origin feature/cha-revert-seed
```

I8 PR에 `Closes #<I8 실제 번호>`를 넣고 송씨의 실질 리뷰와 Approve 후 **Create a merge commit**으로 병합합니다.

### 2단계 · 실제 파일 추가 커밋 찾기

```bash
git switch main
git pull --ff-only origin main
git log --oneline --all -- docs/revert-practice.md
```

출력에서 메시지가 `docs: add temporary revert practice note`인 커밋 hash를 선택합니다. `Merge pull request ...` 커밋이 아니라 실제 파일 추가 커밋인지 다음 명령으로 확인합니다.

```bash
git show --stat <I8_FILE_ADD_COMMIT_HASH>
```

### 3단계 · 별도 브랜치에서 revert

```bash
git switch -c feature/cha-revert-and-submission
git revert --no-edit <I8_FILE_ADD_COMMIT_HASH>
git status
git log --oneline -3
git push -u origin feature/cha-revert-and-submission
```

revert 후 `docs/revert-practice.md`가 사라지고 다른 파일은 영향을 받지 않았는지 확인합니다. 같은 브랜치에서 이 시나리오의 실제 결과와 `SUBMISSION.md`를 보완하여 추가 커밋합니다.

```bash
git add docs/troubleshooting-log.md SUBMISSION.md
git commit -m "docs: record revert practice and submission evidence"
git push
```

### 실제 결과(차씨 작성)

- 실행 날짜: 2026-09-30
- I8 Issue/PR URL: https://github.com/jeenee-cha/b2-2/issues/17 / https://github.com/jeenee-cha/b2-2/pull/18
- 원본 파일 추가 커밋 URL: https://github.com/jeenee-cha/b2-2/commit/765bf661177078fb147f2fed3bbc9938b72cf194
- revert 커밋 URL: https://github.com/jeenee-cha/b2-2/commit/68e84b84dc7529f335137213256d45320ad8cda2
- I9 Issue/PR URL: https://github.com/jeenee-cha/b2-2/issues/21 / PR 생성 후 보완
- 파일 삭제 및 다른 파일 무영향 확인:

```text
$ git show --name-only --oneline 68e84b8
68e84b8 revert: 공유된 실습용 임시 문서 취소
docs/revert-practice.md

$ test ! -e docs/revert-practice.md && echo "revert removed temporary file"
revert removed temporary file

$ git log --oneline -3
68e84b8 revert: 공유된 실습용 임시 문서 취소
b514e49 Merge pull request #20 from jeenee-cha/feature/song-submission-evidence
a7cb38e docs: stash 확인자 재확인 승인 링크 추가
```

- 송씨의 리뷰 및 차씨의 답글/반영 링크: I9 PR 생성 후 보완

### 선택 이유와 주의점

이미 원격과 `main`에 공유된 커밋은 reset으로 지우지 않고 반대 변경을 새 커밋으로 남기는 revert가 안전합니다. 대상이 merge commit이면 `-m` 옵션이 필요하므로, 이번 실습에서는 merge commit이 아니라 그 안의 실제 파일 추가 커밋 hash를 정확히 선택합니다.

## 최종 확인

- [ ] amend 전후 hash와 메시지가 있음
- [ ] reset 전 커밋과 reset 후 staged 상태가 있음
- [ ] stash 목록과 pop 결과가 있음
- [x] 원본 commit과 revert commit URL이 모두 있음
- [ ] 네 시나리오에 차씨, 김씨, 송씨가 각각 실행자로 참여함
- [ ] 모든 명령은 개인 feature 브랜치에서 실행되었고 force push가 없음
