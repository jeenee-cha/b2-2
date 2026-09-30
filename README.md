# B2-2 Git Collaboration Mission

차씨, 김씨, 송씨가 Python 유틸 함수 모음을 만들면서 GitHub Flow를 실제로 연습하는 저장소입니다. 완성된 코드의 복잡도보다 **Issue → feature 브랜치 → 커밋 → PR → 실질 리뷰 → 수정 반영 → 병합 → 증빙 기록**이 모두 남는 것이 더 중요합니다.

## 팀 구성과 책임

| 팀원 | 역할 | 직접 구현 | Git 실습 및 문서 책임 |
| --- | --- | --- | --- |
| 차씨 | 팀 리드 / 저장소 관리자 | `src/list_utils.py` | CONTRIBUTING의 GitHub Flow·브랜치·충돌 대응, Branch Protection, `revert`, 최종 제출 검수 |
| 김씨 | 기능·충돌 기록 담당 | `src/math_utils.py` | CONTRIBUTING의 커밋·복구 규칙, README 같은 hunk 충돌, `commit --amend`, `reset --soft` |
| 송씨 | 기능·검증 담당 | `src/string_utils.py` | CONTRIBUTING의 PR·리뷰 규칙, rename/modify 충돌, `stash` / `stash pop` |

차씨가 진행을 주도하되 김씨와 송씨의 브랜치, 커밋, PR, 리뷰를 대신 만들지 않습니다. 세 사람 모두 병합된 PR 2개 이상, 타인 PR의 실질 리뷰 2개 이상, 본인 PR에서 리뷰 의견 반영 1회 이상을 직접 남깁니다.

`docs/CONTRIBUTING.md`는 차씨 I1, 김씨 I3, 송씨 I4에서 각자 맡은 절을 직접 수정하고 별도 커밋으로 남깁니다. 최종 제출 시 세 사람의 작성 커밋 URL을 `SUBMISSION.md`에 기록합니다.

## 충돌 실습용 팀 목표

우리 팀은 각자의 코드 기여와 리뷰 과정을 중심으로 Git 협업을 연습합니다.

이 문장은 README 같은 hunk 충돌을 만들기 위한 공통 기준선입니다. I5와 I6을 시작하기 전에는 수정하지 않습니다.

## 선택 결과물

간단한 결과물은 **Python 유틸 함수 모음**으로 고정합니다.

| 담당 | 함수 | 동작 | 테스트 핵심 |
| --- | --- | --- | --- |
| 차씨 | `unique_preserve_order(values)` | 목록의 중복을 제거하고 최초 순서를 유지 | 일반 목록, 빈 목록 |
| 김씨 | `clamp(value, minimum, maximum)` | 숫자를 최솟값과 최댓값 사이로 제한 | 범위 안/밖, 역전된 범위 |
| 송씨 | `normalize_whitespace(text)` | 연속 공백과 줄바꿈을 한 칸으로 정리 | 일반 문자열, 빈 문자열, 비문자열 |

초기 배포본의 `src/`에는 안내 문서만 있습니다. 실제 `.py` 파일과 테스트는 각 담당자가 자기 Issue와 feature 브랜치에서 만들어야 개인 기여 커밋과 PR 증빙이 남습니다.

## 협업 문서 사용 순서

1. [협업 규칙](docs/CONTRIBUTING.md)을 모든 PR에 적용합니다.
2. 실제 충돌 직후 [충돌 해결 기록지](docs/conflict-resolution.md)를 채웁니다.
3. Git 복구 명령 직후 [트러블슈팅 기록지](docs/troubleshooting-log.md)를 채웁니다.
4. PR을 병합할 때마다 [최종 제출 인덱스](SUBMISSION.md)에 URL을 기록합니다.

## 반드시 지킬 운영 규칙

- 최초 저장소 세팅 커밋을 push한 직후 `main` Branch Protection을 설정합니다.
- 보호 설정 이후 `main`에는 직접 push하지 않고 모든 변경을 PR로 병합합니다.
- 작업마다 Issue를 만들고 PR 본문에 `Closes #실제번호`를 넣습니다.
- PR 본문에는 What, Why, How를 모두 작성합니다.
- 모든 PR에는 파일이나 줄을 근거로 한 실질 리뷰와 작성자의 답글 또는 수정 반영이 있어야 합니다.
- 공유 브랜치에서 `push --force`, `reset`, 합의 없는 rebase를 사용하지 않습니다.
- 충돌용 김씨·송씨 브랜치는 차씨의 충돌 기준 PR이 병합되기 **전에** 먼저 만들어 push합니다.
- 문서의 `<...>`와 `TODO`는 최종 제출 전에 실제 Issue, PR, 리뷰, 커밋 URL 및 명령 출력으로 교체합니다.

## 저장소 구조

```text
b2-2/
├── .github/
│   ├── ISSUE_TEMPLATE/task.md
│   └── pull_request_template.md
├── docs/
│   ├── CONTRIBUTING.md
│   ├── conflict-demo.md
│   ├── conflict-resolution.md
│   └── troubleshooting-log.md
├── src/
├── README.md
└── SUBMISSION.md
```

`docs/conflict-demo.md`는 rename/modify 충돌 전용 파일입니다. 실습이 끝나면 `docs/merge-conflict-demo.md`라는 이름으로 남습니다.

## 완료 조건

- [ ] 차씨, 김씨, 송씨 모두 병합된 PR 2개 이상
- [ ] 세 사람 모두 타인 PR의 실질 리뷰 2개 이상
- [ ] 세 사람 모두 본인 PR에서 리뷰 반영 1회 이상
- [ ] 모든 PR에 `Closes #`, What, Why, How, 실질 리뷰, 상호작용 존재
- [ ] 같은 hunk 충돌과 rename/modify 충돌을 각각 해결하고 기록
- [ ] `amend`, `reset --soft`, `revert`, `stash/pop`을 실제로 실행하고 기록
- [ ] Branch Protection 설정과 `git log --oneline --graph --all` 증빙 확보
- [ ] `SUBMISSION.md`의 모든 자리표시자를 실제 링크로 교체
