# Conflict Resolution Log

이 문서는 I5, I6, I7에서 실제로 발생한 충돌을 기록합니다. `<실행 후 ...>` 자리에는 터미널 출력, GitHub URL, 실제 커밋 hash를 넣습니다. 충돌이 발생하지 않았다면 완료한 것처럼 쓰지 말고 브랜치 생성 시점과 수정한 줄이 계획과 같았는지 먼저 확인합니다.

## 공통 선행 조건

- 김씨의 `feature/kim-conflict-troubleshooting`과 송씨의 `feature/song-conflict-troubleshooting`은 I5가 병합되기 전에 최신 `main`에서 만들어져야 합니다.
- 두 브랜치가 충돌 대상 변경을 commit하고 원격에 push한 것을 확인한 뒤 I5를 병합합니다.
- I5 브랜치: `feature/cha-conflict-baseline`
- 공유 브랜치 rebase 또는 force push는 사용하지 않습니다.

---

## 충돌 기록 #1 · README 같은 hunk

### 참여자와 관련 작업

- 충돌 변경 작성자·해결자: 김씨
- 기준 변경 작성자: 차씨
- 검증자: 차씨
- 김씨 Issue/PR: `<I6 Issue URL>` / `<I6 PR URL>`
- 차씨 기준 Issue/PR: `<I5 Issue URL>` / `<I5 PR URL>`

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
git commit --amend -m "docs: prepare Kim version of project description"
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
<실행 후 README.md가 both modified로 표시된 부분을 붙여넣기>
```

실제 충돌 마커:

```text
<<<<<<< HEAD
<김씨 브랜치의 실제 문장>
=======
<origin/main에서 들어온 차씨 문장>
>>>>>>> origin/main
```

### 합의한 최종 내용

두 의도를 모두 살린 아래 문장으로 정리하고 충돌 마커를 모두 삭제합니다.

```text
우리 팀은 Issue부터 PR 병합까지 전 과정을 재현하고, 각자의 코드 기여와 리뷰 과정을 통해 GitHub Flow를 연습합니다.
```

```bash
git add README.md docs/conflict-resolution.md
git commit -m "docs: resolve same-hunk README conflict"
python3 -m unittest discover -s tests -v
git push
```

### 결과(실행 후 작성)

- 충돌 발생 날짜: `<YYYY-MM-DD>`
- 해결 커밋 URL: `<commit URL>`
- 병합된 I6 PR URL: `<PR URL>`
- 테스트 결과: `<tests run, failures>`
- 선택 이유: 차씨의 GitHub Flow 설명과 김씨의 개인 기여·리뷰 목적을 모두 보존하기 위해 두 문장을 합쳤습니다.
- 배운 점: `<실제 배운 점>`

---

## 충돌 기록 #2 · rename/modify와 같은 문단 수정

### 참여자와 관련 작업

- 내용 변경 작성자·해결자: 송씨
- 파일 rename 및 기준 변경 작성자: 차씨
- 검증자: 김씨
- 송씨 Issue/PR: `<I7 Issue URL>` / `<I7 PR URL>`
- 차씨 기준 Issue/PR: `<I5 Issue URL>` / `<I5 PR URL>`

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
git commit -m "docs: prepare Song version of conflict demo"
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

`git status` 또는 Git의 `CONFLICT` 출력:

```text
<실행 후 rename/modify 또는 content conflict 관련 출력을 붙여넣기>
```

충돌 마커가 생성됐다면 실제 내용을 붙여넣습니다.

```text
<<<<<<< HEAD
<송씨 브랜치 내용>
=======
<차씨가 rename하면서 수정한 내용>
>>>>>>> origin/main
```

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
git commit -m "docs: preserve demo content after file rename"
python3 -m unittest discover -s tests -v
git push
```

### 결과(실행 후 작성)

- 충돌 발생 날짜: `<YYYY-MM-DD>`
- 해결 커밋 URL: `<commit URL>`
- 병합된 I7 PR URL: `<PR URL>`
- 최종 파일 URL: `<docs/merge-conflict-demo.md URL>`
- 테스트 결과: `<tests run, failures>`
- 선택 이유: rename 의도와 송씨의 내용 변경을 모두 보존하기 위해 새 경로에 합친 내용을 남겼습니다.
- 배운 점: `<실제 배운 점>`

## 기록 완료 확인

- [ ] 두 충돌 모두 실제 `git status` 또는 충돌 마커가 있음
- [ ] 해결 전략과 선택 이유가 있음
- [ ] 해결 커밋과 병합 PR URL이 있음
- [ ] 테스트 또는 문서 검증 결과가 있음
- [ ] 차씨, 김씨, 송씨의 역할이 기록에 드러남
