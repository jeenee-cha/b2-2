# Contributing Guide

> 이 문서는 팀 작업 시작을 위한 부트스트랩 규칙입니다. 세부 규칙은 차씨 I1, 김씨 I3, 송씨 I4 PR에서 분담하여 완성합니다.

## 1. 초기 GitHub Flow

- `main`은 테스트가 통과하고 문서 링크가 정상인 상태만 유지합니다.
- 최초 저장소 설정 이후 `main` 직접 push를 금지합니다.
- 모든 작업은 Issue 하나에 대응하는 `feature/*` 브랜치에서 진행합니다.
- 모든 feature 브랜치는 최소 1명의 승인을 받은 PR로 병합합니다.
- 병합은 Git 그래프 증빙을 위해 **Create a merge commit**을 사용합니다.

## 2. 브랜치 네이밍

형식:

```text
feature/<담당자>-<작업>
```

담당자 이름:

- 차씨: `cha`
- 김씨: `kim`
- 송씨: `song`

예시:

```text
feature/cha-contributing-guide
feature/cha-list-utils
feature/kim-math-utils
feature/song-string-utils
```

작업 시작:

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/<담당자>-<작업>
```

- 영문 소문자와 하이픈만 사용합니다.
- 한 브랜치에서는 한 Issue만 해결합니다.
- 이미 병합된 브랜치를 다른 작업에 재사용하지 않습니다.

## 3. 초기 커밋 메시지 규칙

형식:

```text
<type>: <구체적인 변경 대상과 효과>
```

| type | 사용 시점 | 예시 |
| --- | --- | --- |
| `feat` | 기능 추가 | `feat: add clamp utility` |
| `fix` | 잘못된 동작 수정 | `fix: reject inverted bounds in clamp utility` |
| `docs` | 문서와 증빙 변경 | `docs: clarify pull request review rules` |
| `test` | 테스트 추가·수정 | `test: cover empty input in list utils` |
| `refactor` | 동작을 유지한 구조 개선 | `refactor: simplify whitespace normalization` |
| `chore` | 초기 설정·보조 작업 | `chore: initialize Git collaboration mission` |

금지 예:

```text
update
fix
temp
wip
final
bug fix
edit file
```

## 4. 작업 시작 규칙

1. GitHub Issue를 먼저 만들고 본인을 Assignee로 지정합니다.
2. 최신 `main`에서 feature 브랜치를 만듭니다.
3. 구체적인 메시지로 commit합니다.
4. 원격 feature 브랜치에 push하고 PR을 만듭니다.
5. PR 본문에 `Closes #<실제 Issue 번호>`를 작성합니다.
6. 최소 1명의 실질 review와 Approve를 받은 뒤 병합합니다.

PR 본문에는 최소 다음 항목을 포함합니다.

```markdown
## 연결 이슈
- Closes #<실제 Issue 번호>

## 변경 사항(What)
- <무엇을 바꿨는가>

## 변경 이유(Why)
- <왜 바꿨는가>

## 테스트/검증 방법(How)
- `<실행 명령>` → `<실제 결과>`
```

## 5. PR에서 완성할 담당 구역

| 담당 | 계획 ID | 완성할 내용 | 예정 커밋 |
| --- | --- | --- | --- |
| 차씨 | I1 | GitHub Flow 선택 이유, 브랜치 상세 규칙, 충돌 대응 흐름 | `docs: define GitHub Flow collaboration rules` |
| 김씨 | I3 | 커밋 메시지 상세 규칙, amend/reset/revert/stash 안전 기준 | `docs: clarify commit and recovery rules` |
| 송씨 | I4 | PR 본문 상세 규칙, 실질 리뷰 기준, 답글·재확인 절차 | `docs: clarify pull request review rules` |

리뷰만 한 경우는 작성 분담으로 계산하지 않습니다. 세 사람 모두 이 파일을 직접 수정한 커밋 URL을 `SUBMISSION.md`에 기록합니다.
