# Contributing Guide

> 이 문서는 차씨, 김씨, 송씨가 함께 적용하는 협업 규칙입니다. 차씨 I1에서 공통 운영 기준을 확정하고, 김씨 I3와 송씨 I4에서 담당 세부 규칙을 완성합니다.

## 1. GitHub Flow와 팀 적용값

| 항목 | 적용값 |
| --- | --- |
| 저장소 | `https://github.com/jeenee-cha/b2-2` |
| 적용 시작일 | 2026-09-30 |
| 기본 브랜치 | `main` |
| 작업 브랜치 | `feature/<담당자>-<작업>` |
| 병합 방식 | Create a merge commit |
| 보호 규칙 | PR 필수, 승인 1명 이상, 대화 해결 필수, force push·삭제 금지 |

- `main`은 테스트가 통과하고 문서 링크가 정상인 상태만 유지합니다.
- 최초 저장소 설정 이후 `main` 직접 push를 금지합니다.
- 모든 작업은 Issue 하나에 대응하는 `feature/*` 브랜치에서 진행합니다.
- 모든 feature 브랜치는 최소 1명의 승인을 받은 PR로 병합합니다.
- 병합은 Git 그래프 증빙을 위해 **Create a merge commit**을 사용합니다.

GitHub Flow를 선택한 이유:

1. 세 명이 짧은 feature 브랜치로 작업하면 담당 범위와 변경 이력이 명확합니다.
2. `main`을 안정적으로 유지하면서 PR 리뷰와 승인 과정을 강제할 수 있습니다.
3. Issue, PR, review를 연결해 과제의 협업 과정과 개인 기여를 증빙할 수 있습니다.

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

## 3. 커밋 메시지 기본 규칙

형식:

```text
<영문 type>: <구체적인 한글 변경 대상과 효과>
```

- type은 영어 소문자로 작성하고 콜론 뒤 설명은 한글로 작성합니다.
- 명령어, 파일명, 함수명 같은 고유 식별자는 원문 표기를 허용합니다.
- amend, reset, revert, stash의 상세 안전 기준은 김씨가 I3에서 추가합니다.

| type | 사용 시점 | 예시 |
| --- | --- | --- |
| `feat` | 기능 추가 | `feat: 숫자 범위 제한 유틸리티 추가` |
| `fix` | 잘못된 동작 수정 | `fix: 문자열 유틸리티의 비문자열 입력 거부` |
| `docs` | 문서와 증빙 변경 | `docs: 풀 리퀘스트 리뷰 규칙 명확화` |
| `test` | 테스트 추가·수정 | `test: 목록 유틸리티의 빈 입력 검증 추가` |
| `refactor` | 동작을 유지한 구조 개선 | `refactor: 공백 정규화 로직 단순화` |
| `chore` | 초기 설정·보조 작업 | `chore: Git 협업 미션 초기 설정` |
| `revert` | 공유된 변경 되돌리기 | `revert: 되돌리기 실습용 임시 문서 취소` |

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

PR 제목도 커밋 메시지와 같은 언어 규칙을 적용합니다.

```text
<영문 type>: <구체적인 한글 작업 요약>
```

Create a merge commit을 선택할 때 merge commit 제목도 `chore: PR #<번호> <한글 작업 요약> 병합` 형식으로 수정합니다.

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

## 5. 충돌 발생 시 기본 대응 흐름

1. 충돌이 발생한 브랜치의 작성자가 PR 또는 팀 채널에 충돌 파일과 상태를 공유합니다.
2. 양쪽 변경 작성자가 각 변경의 의도를 확인하기 전에는 한쪽 내용을 임의로 삭제하지 않습니다.
3. 현재 feature 브랜치 작성자가 해결을 담당하고, 상대 변경 작성자는 해결 커밋이 push된 후 PR 병합 전에 최종 내용이 의도와 맞는지 리뷰 코멘트로 확인합니다.
4. 해결 전 `git status`, 충돌 마커, 실행 명령과 선택 이유를 `docs/conflict-resolution.md`에 기록합니다.
5. 해결 후 전체 테스트와 파일 경로를 검증하고, 리뷰어가 기록과 최종 결과를 재확인합니다.
6. 공유 브랜치에서는 force push, reset, 합의 없는 rebase로 충돌을 우회하지 않습니다.

## 6. PR에서 완성할 담당 구역

| 담당 | 계획 ID | 완성할 내용 | 예정 커밋 |
| --- | --- | --- | --- |
| 차씨 | I1 | GitHub Flow 선택 이유, 브랜치 상세 규칙, 충돌 대응 흐름 | `docs: 팀의 GitHub Flow 협업 규칙 정의` |
| 김씨 | I3 | 커밋 메시지 상세 규칙, amend/reset/revert/stash 안전 기준 | `docs: 커밋 및 복구 규칙 명확화` |
| 송씨 | I4 | PR 본문 상세 규칙, 실질 리뷰 기준, 답글·재확인 절차 | `docs: 풀 리퀘스트 리뷰 규칙 명확화` |

리뷰만 한 경우는 작성 분담으로 계산하지 않습니다. 세 사람 모두 이 파일을 직접 수정한 커밋 URL을 `SUBMISSION.md`에 기록합니다.
