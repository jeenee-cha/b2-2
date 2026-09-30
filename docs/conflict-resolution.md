# Conflict Resolution Log

이 문서는 I5, I6, I7에서 실제로 발생한 충돌을 기록합니다. `<실행 후 ...>` 자리에는 터미널 출력, GitHub URL, 실제 커밋 hash를 넣습니다. 충돌이 발생하지 않았다면 완료한 것처럼 쓰지 말고 브랜치 생성 시점과 수정한 줄이 계획과 같았는지 먼저 확인합니다.

## 공통 선행 조건

- 김씨의 `feature/kim-conflict-troubleshooting`과 송씨의 `feature/song-conflict-troubleshooting`은 I5가 병합되기 전에 최신 `main`에서 만들어져야 합니다.
- 두 브랜치가 충돌 대상 변경을 commit하고 원격에 push한 것을 확인한 뒤 I5를 병합합니다.
- I5가 병합되기 전에는 I6·I7 브랜치에서 `origin/main`을 merge하지 않습니다. 두 브랜치의 분기점을 기준 SHA로 유지하고, I5 병합 후 최초 merge에서 의도한 충돌을 재현하기 위해서입니다.
- I5 브랜치: `feature/cha-conflict-baseline`
- 공유 브랜치 rebase 또는 force push는 사용하지 않습니다.

차씨는 I5를 시작하기 전에 다음 명령으로 두 원격 브랜치와 공통 기준 SHA를 확인합니다.

```bash
git fetch origin
git ls-remote --heads origin feature/kim-conflict-troubleshooting feature/song-conflict-troubleshooting
git rev-parse --short origin/main
git rev-parse --short "$(git merge-base origin/main origin/feature/kim-conflict-troubleshooting)"
git rev-parse --short "$(git merge-base origin/main origin/feature/song-conflict-troubleshooting)"
```

마지막 세 명령의 결과는 모두 I4 병합 직후 기준 SHA인 `82df3ef`이어야 합니다.

---

## 충돌 기록 #1 · README 같은 hunk

### 참여자와 관련 작업

- 충돌 변경 작성자·해결자: 김씨
- 기준 변경 작성자: 차씨
- 검증자: 차씨
- 김씨 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/12` / `https://github.com/jeenee-cha/b2-2/pull/15`
- 차씨 기준 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/13` / `https://github.com/jeenee-cha/b2-2/pull/14`

### 재현용 변경

두 사람은 I5 병합 전에 `README.md`의 `충돌 실습용 팀 목표` 아래 같은 문장을 서로 다르게 수정합니다.

김씨 브랜치 문장:

```text
우리 팀은 각자의 코드 기여와 리뷰 과정을 중심으로 Git 협업을 연습합니다.
```

차씨 I5 브랜치 문장:

```text
우리 팀은 Issue부터 PR 병합까지 전 과정을 재현하며 GitHub Flow를 연습합니다.
```

김씨는 I5 병합 전에 다음 상태까지 완료합니다.

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/kim-conflict-troubleshooting
# VS Code에서 README.md의 지정 문장을 김씨 문장으로 수정
git add README.md
git commit -m "docs: update"
git log --oneline -1
git commit --amend -m "docs: 김씨 버전 프로젝트 설명 준비"
git log --oneline -1
git push -u origin feature/kim-conflict-troubleshooting
```

차씨가 I5를 리뷰받아 `main`에 병합한 뒤 김씨가 다음을 실행합니다.

```bash
git switch feature/kim-conflict-troubleshooting
git fetch origin
git merge origin/main
git status
```

### 실제 충돌 증빙

`git status` 관련 출력:

```text
$ git rev-parse --short origin/main
8432dbd
$ git merge origin/main
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status
On branch feature/kim-conflict-troubleshooting
Your branch is ahead of 'origin/feature/kim-conflict-troubleshooting' by 1 commit.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	modified:   docs/conflict-resolution.md
	renamed:    docs/conflict-demo.md -> docs/merge-conflict-demo.md

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   README.md
```

실제 충돌 마커:

```text
<<<<<<< HEAD
우리 팀은 각자의 코드 기여와 리뷰 과정을 중심으로 Git 협업을 연습합니다.
=======
우리 팀은 Issue부터 PR 병합까지 전 과정을 재현하며 GitHub Flow를 연습합니다.
>>>>>>> origin/main
```

### 합의한 최종 내용

두 의도를 모두 살린 아래 문장으로 정리하고 충돌 마커를 모두 삭제합니다.

```text
우리 팀은 Issue부터 PR 병합까지 전 과정을 재현하고, 각자의 코드 기여와 리뷰 과정을 통해 GitHub Flow를 연습합니다.
```

```bash
git add README.md docs/conflict-resolution.md
python3 -m unittest discover -s tests -v
grep -n "<<<<<<<\|=======\|>>>>>>>" README.md
git commit -m "docs: README 같은 hunk 충돌 해결"
git push
```

### 결과(실행 후 작성)

- 충돌 발생 날짜: `2026-09-30`
- 충돌 당시 김씨 브랜치 HEAD / 병합한 `origin/main`: `51797dc` / `8432dbd`
- 해결 커밋 URL: `https://github.com/jeenee-cha/b2-2/commit/fb02e6887babc6891ae113ef32b60501eb5f9e55`
- 병합된 I6 PR URL: `https://github.com/jeenee-cha/b2-2/pull/15` (리뷰 중, 병합 후 갱신)
- 테스트 결과: `Ran 9 tests ... OK`, README 충돌 마커 검색 결과 없음
- 선택 이유: 차씨의 GitHub Flow 설명과 김씨의 개인 기여·리뷰 목적을 모두 보존하기 위해 두 문장을 합쳤습니다.
- 배운 점: 같은 줄을 양쪽이 다르게 바꾸면 Git이 자동으로 고르지 않고 해당 파일만 `Unmerged paths`로 멈춥니다. 같은 merge에서 겹치지 않는 변경(`docs/conflict-resolution.md`, rename)은 자동으로 합쳐져 staged 상태로 들어오므로, 해결할 파일은 `git status`의 `both modified`로 좁혀 확인하면 됩니다.

---

## 충돌 기록 #2 · rename/modify와 같은 문단 수정

### 참여자와 관련 작업

- 내용 변경 작성자·해결자: 송씨
- 파일 rename 및 기준 변경 작성자: 차씨
- 검증자: 김씨
- 송씨 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/11` / `(PR 생성 후 갱신)`
- 차씨 기준 Issue/PR: `https://github.com/jeenee-cha/b2-2/issues/13` / `https://github.com/jeenee-cha/b2-2/pull/14`

### 재현용 변경

기준 파일은 `docs/conflict-demo.md`입니다. 송씨는 기존 파일의 `Shared Message`를 다음처럼 수정합니다.

```text
송씨는 내용 수정 담당으로 충돌 해결 과정을 기록합니다.
```

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/song-conflict-troubleshooting
# VS Code에서 docs/conflict-demo.md의 Shared Message 수정
git add docs/conflict-demo.md
git commit -m "docs: 충돌 실습 문서의 송씨 공유 메시지 작성"
git push -u origin feature/song-conflict-troubleshooting
```

그 뒤 차씨는 I5에서 같은 기준의 `main`으로부터 파일을 rename하고 같은 문단을 다르게 수정합니다.

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/cha-conflict-baseline
git mv docs/conflict-demo.md docs/merge-conflict-demo.md
# VS Code에서 Shared Message를 아래 차씨 문장으로 수정
git add README.md docs/merge-conflict-demo.md
git commit -m "docs: prepare intentional conflict baseline"
git push -u origin feature/cha-conflict-baseline
```

차씨 문장:

```text
차씨는 파일 이동 담당으로 rename/modify 충돌을 준비합니다.
```

I5와 I6가 병합된 뒤 송씨가 다음을 실행합니다.

```bash
git switch feature/song-conflict-troubleshooting
git fetch origin
git merge origin/main
git status
```

### 실제 충돌 증빙

`git status` 또는 Git의 `CONFLICT` 출력(병합 직전 송씨 브랜치 HEAD `e251744`, `origin/main` `ae9ee58`):

```text
$ git fetch origin
$ git merge origin/main
Auto-merging docs/merge-conflict-demo.md
CONFLICT (content): Merge conflict in docs/merge-conflict-demo.md
Automatic merge failed; fix conflicts and then commit the result.

$ git status
On branch feature/song-conflict-troubleshooting
Your branch is up to date with 'origin/feature/song-conflict-troubleshooting'.

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	modified:   README.md
	modified:   SUBMISSION.md
	deleted:    docs/conflict-demo.md
	modified:   docs/conflict-resolution.md
	modified:   docs/troubleshooting-log.md

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   docs/merge-conflict-demo.md
```

충돌 마커가 생성됐다면 실제 내용을 붙여넣습니다.

```text
<<<<<<< HEAD:docs/conflict-demo.md
송씨는 내용 수정 담당으로 충돌 해결 과정을 기록합니다.
=======
차씨는 파일 이동 담당으로 rename/modify 충돌을 준비합니다.
>>>>>>> origin/main:docs/merge-conflict-demo.md
```

Git이 `docs/conflict-demo.md` → `docs/merge-conflict-demo.md` rename을 감지해 송씨 변경을 새 경로로 옮긴 뒤, 같은 `Shared Message` 줄에서 content 충돌을 표시했습니다. 마커의 `HEAD:docs/conflict-demo.md`와 `origin/main:docs/merge-conflict-demo.md`가 각각 이전 경로와 새 경로를 가리킵니다.

### 합의한 최종 내용

- 최종 파일명: `docs/merge-conflict-demo.md`
- 기존 `docs/conflict-demo.md`는 남기지 않습니다.
- `Shared Message`는 아래처럼 두 의도를 합칩니다.

```text
차씨는 파일 이동, 송씨는 내용 수정을 맡아 rename/modify 충돌 해결 과정을 함께 기록합니다.
```

```bash
git add -A -- docs/conflict-demo.md docs/merge-conflict-demo.md
git add docs/conflict-resolution.md docs/troubleshooting-log.md
python3 -m unittest discover -s tests -v
grep -n "<<<<<<<\|=======\|>>>>>>>" docs/merge-conflict-demo.md
git commit -m "docs: rename/modify 충돌 해결"
git push
```

### 결과(실행 후 작성)

- 충돌 발생 날짜: `2026-09-30`
- 충돌 당시 송씨 브랜치 HEAD / 병합한 `origin/main`: `e251744` / `ae9ee58` (분기점 `82df3ef`)
- 해결 커밋 URL: `(push 후 갱신)`
- 병합된 I7 PR URL: `(PR 생성 후 갱신)`
- 최종 파일 URL: `https://github.com/jeenee-cha/b2-2/blob/main/docs/merge-conflict-demo.md`
- 최종 파일 확인: `docs/conflict-demo.md`는 삭제되고 `docs/merge-conflict-demo.md`만 남음, 충돌 마커 검색 결과 없음
- 테스트 결과: `Ran 9 tests ... OK`
- 선택 이유: rename 의도와 송씨의 내용 변경을 모두 보존하기 위해 새 경로에 합친 내용을 남겼습니다.
- 배운 점: 한쪽이 파일을 옮기고 다른 쪽이 옛 경로에서 내용을 바꿔도, 내용이 충분히 비슷하면 Git이 rename을 추적해 변경을 새 경로로 옮겨 합칩니다. 이번에는 같은 줄까지 바뀌어 `both modified: docs/merge-conflict-demo.md`로 멈췄으므로, 새 경로에서 두 문장을 합치고 옛 경로가 다시 생기지 않았는지 `git status`로 확인하는 것이 핵심이었습니다.

## 기록 완료 확인

- [ ] 두 충돌 모두 실제 `git status` 또는 충돌 마커가 있음
- [ ] 해결 전략과 선택 이유가 있음
- [ ] 해결 커밋과 병합 PR URL이 있음
- [ ] 테스트 또는 문서 검증 결과가 있음
- [ ] 차씨, 김씨, 송씨의 역할이 기록에 드러남
