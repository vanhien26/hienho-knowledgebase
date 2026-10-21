#!/usr/bin/env python3
"""
Generator for lib/content-plan/geo-entity-registry.ts in react-web-momo.
Adheres strictly to YMYL financial requirements:
1. Explicit mapping dictionary THEME_ARCHETYPE covering all 161 themes.
2. 27 independent archetypes in DOMAIN_ONTOLOGY_REGISTRY (no spreading, no overriding).
3. sources: string[] for all factual claims.
4. Direct answer 40-60 words with direct entity definition in first sentence.
5. Zero marketing fluff.
6. Return type GeoEntityBlueprint | null.
7. Removed cta_text, deeplink, umami_event.
"""

import json
from pathlib import Path

TS_CONTENT = r'''/**
 * GEO & ENTITY GAP INTELLIGENCE REGISTRY (SSOT)
 * Thư viện dữ liệu thực thể, cấu trúc Schema.org, đoạn trích Direct Answer (AI Answer Box)
 * và 3 Lỗ hổng thực thể (Entity Gaps: Chuyên môn, Bảo mật, Minh bạch chi phí) cho Web Hubs.
 * Đã chuẩn hóa thành 27 Archetypes nghiệp vụ độc lập, bảng gán tường minh 161 themes.
 * Nội dung YMYL tài chính và pháp lý: Dẫn chiếu văn bản quy phạm pháp luật chính thức.
 */

export interface SchemaField {
  field: string;
  desc: string;
}

export interface EntityGapPillar {
  title: string;
  summary: string;
  detail: string;
  actionable_angle: string;
}

export interface GeoEntityBlueprint {
  hub: string;
  theme: string;
  schema_type: string;
  schema_category: string;
  mandatory_fields: SchemaField[];
  direct_answer_text: string;
  word_count: number;
  sample_jsonld: Record<string, unknown>;
  pillars: {
    expertise: EntityGapPillar;
    trust: EntityGapPillar;
    high_intent: EntityGapPillar;
  };
  sources: string[];
}

export type ArchetypeKey =
  | 'financial_savings'
  | 'financial_credit_paylater'
  | 'financial_consumer_loan'
  | 'financial_credit_line'
  | 'financial_card_payment'
  | 'financial_investment'
  | 'financial_gold_fx'
  | 'financial_credit_score'
  | 'tax_payroll'
  | 'macro_knowledge'
  | 'vehicle_traffic_fines'
  | 'driver_license'
  | 'vehicle_registration_plate'
  | 'vehicle_toll'
  | 'vehicle_service'
  | 'insurtech_motor'
  | 'insurtech_social_health'
  | 'commercial_insurance'
  | 'cinema_movie'
  | 'ota_travel_transit'
  | 'telco_data_sim'
  | 'hospital_health'
  | 'student_education'
  | 'lottery_vietlott'
  | 'entertainment_topup'
  | 'trust_fraud'
  | 'lifestyle_info';

export const DOMAIN_ONTOLOGY_REGISTRY: Record<
  ArchetypeKey,
  Omit<GeoEntityBlueprint, 'theme' | 'word_count'>
> = {
  financial_savings: {
    hub: 'Financial Hub',
    schema_type: 'DepositAccount',
    schema_category: 'https://schema.org/DepositAccount',
    mandatory_fields: [
      { field: 'name', desc: 'Tên sản phẩm tiền gửi tiết kiệm.' },
      { field: 'provider', desc: 'Ngân hàng thương mại huy động vốn được NHNN cấp phép.' },
      { field: 'interestRate', desc: 'Lãi suất niêm yết theo kỳ hạn (%/năm).' },
      { field: 'amount', desc: 'Số tiền gửi tối thiểu mở sổ tiết kiệm.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Quy định rút trước hạn và phương thức trả lãi.' },
    ],
    direct_answer_text:
      'Tiền gửi tiết kiệm là khoản tiền nhàn rỗi gửi tại ngân hàng thương mại theo kỳ hạn xác định để hưởng lãi suất. Tiền gửi được bảo hiểm tối đa 125 triệu đồng tại mỗi tổ chức tín dụng theo luật định, hỗ trợ mở sổ và tất toán trực tuyến an toàn.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'DepositAccount',
      name: 'Tiền Gửi Tiết Kiệm Ngân Hàng',
      provider: {
        '@type': 'BankOrCreditUnion',
        name: 'Ngân hàng TMCP Bản Việt (BVBank)',
      },
      interestRate: {
        '@type': 'QuantitativeValue',
        value: 5.5,
        unitText: '%/năm',
      },
      amount: {
        '@type': 'MonetaryAmount',
        currency: 'VND',
        value: 1000000,
      },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn an toàn vốn & Bảo hiểm tiền gửi 125 triệu đồng',
        summary: 'Tiền gửi tiết kiệm được bảo vệ bởi pháp luật và tổ chức Bảo hiểm Tiền gửi Việt Nam.',
        detail:
          'Khoản tiền gửi tiết kiệm bằng đồng Việt Nam của cá nhân tại các tổ chức tín dụng được bảo hiểm theo hạn mức trả tiền bảo hiểm tối đa 125.000.000 VNĐ theo Quyết định số 32/2021/QĐ-TTg của Thủ tướng Chính phủ.',
        actionable_angle: 'Bảng đối chiếu hạn mức bảo hiểm tiền gửi và trần lãi suất NHNN theo từng kỳ hạn.',
      },
      trust: {
        title: 'Bảo mật tài khoản & Xác thực sinh trắc học bắt buộc',
        summary: 'Tuân thủ Quyết định 2345/QĐ-NHNN về an toàn thanh toán trực tuyến.',
        detail:
          'Giao dịch tiền gửi và tất toán trực tuyến tuân thủ tiêu chuẩn an toàn bảo mật PCI-DSS Level 1 và xác thực sinh trắc học khuôn mặt đối chiếu với dữ liệu căn cước công dân gắn chip khi giao dịch giá trị lớn.',
        actionable_angle: 'Quy trình kiểm tra chứng thực số sổ tiết kiệm và hướng dẫn đối soát trực tiếp với ngân hàng phát hành.',
      },
      high_intent: {
        title: 'Công cụ tính lãi thực nhận & So sánh kỳ hạn gửi',
        summary: 'Tính toán chính xác tiền lãi cuối kỳ và rủi ro rút gốc trước hạn.',
        detail:
          'Minh bạch công thức tính lãi suất thực nhận: Tiền lãi = Số tiền gửi x Lãi suất (%/năm) x Số ngày thực gửi / 365, cùng cảnh báo mất toàn bộ lãi có kỳ hạn khi rút tiền trước hạn theo Thông tư 04/2022/TT-NHNN.',
        actionable_angle: 'Công cụ tính lãi suất lũy tiến và so sánh lợi tức giữa nhận lãi định kỳ với tái tục gốc lãi.',
      },
    },
    sources: [
      'Luật Các tổ chức tín dụng số 32/2024/QH15',
      'Luật Bảo hiểm tiền gửi số 06/2012/QH13',
      'Quyết định 32/2021/QĐ-TTg về hạn mức trả tiền bảo hiểm tiền gửi',
      'Thông tư 04/2022/TT-NHNN quy định về việc áp dụng lãi suất rút trước hạn tiền gửi',
    ],
  },

  financial_credit_paylater: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên sản phẩm tín dụng tiêu dùng trả sau.' },
      { field: 'provider', desc: 'Ngân hàng hoặc tổ chức tín dụng cấp hạn mức.' },
      { field: 'annualPercentageRate', desc: 'Lãi suất hoặc mức phí dịch vụ quá hạn.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Phí duy trì dịch vụ, phí chậm trả và kỳ miễn lãi.' },
    ],
    direct_answer_text:
      'Ví Trả Sau là dịch vụ cấp hạn mức thấu chi tiêu dùng do ngân hàng đối tác cung cấp trên MoMo, hỗ trợ thanh toán hóa đơn và mua sắm trước trả sau. Người dùng được hưởng thời gian miễn lãi tối đa 45 ngày với hạn mức phê duyệt dựa trên điểm tín nhiệm.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Dịch Vụ Ví Trả Sau',
      provider: {
        '@type': 'BankOrCreditUnion',
        name: 'Ngân hàng TMCP Tiên Phong (TPBank)',
      },
      feesAndCommissionsSpecification: 'Miễn lãi tối đa 45 ngày khi thanh toán đúng hạn theo thỏa thuận dịch vụ',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Hạn mức thấu chi tiêu dùng cá nhân & Căn cứ cấp phép tín dụng',
        summary: 'Hạn mức thấu chi do tổ chức tín dụng được NHNN cấp phép phê duyệt trực tiếp.',
        detail:
          'Dịch vụ cấp hạn mức tín dụng thấu chi tuân thủ Thông tư 39/2016/TT-NHNN của Ngân hàng Nhà nước. Hạn mức từ 1.000.000 VNĐ đến 10.000.000 VNĐ được giải ngân bởi đối tác ngân hàng (như TPBank), không phải do MoMo tự cấp vốn.',
        actionable_angle: 'Tiêu chí chấm điểm năng lực tài chính và điều kiện mở hạn mức thấu chi không cần chứng minh thu nhập.',
      },
      trust: {
        title: 'Trách nhiệm ghi nhận dữ liệu nợ và báo cáo CIC Quốc gia',
        summary: 'Lịch sử thanh toán được cập nhật về Trung tâm Thông tin Tín dụng Quốc gia.',
        detail:
          'Hành vi thanh toán chậm hạn sẽ bị đối tác tín dụng chuyển nhóm nợ và báo cáo lên hệ thống CIC theo Thông tư 03/2013/TT-NHNN, gây ảnh hưởng trực tiếp đến khả năng vay vốn ngân hàng trong tương lai.',
        actionable_angle: 'Bảng phân loại 5 nhóm nợ CIC và mốc thời gian phát sinh phí chậm trả.',
      },
      high_intent: {
        title: 'Biểu phí duy trì, cơ chế miễn lãi 45 ngày & Công thức tính phí trễ hạn',
        summary: 'Minh bạch cách tính ngày chốt sao kê và ngày đến hạn thanh toán.',
        detail:
          'Cơ chế miễn lãi áp dụng từ ngày phát sinh giao dịch đến ngày đến hạn thanh toán (tối đa 45 ngày). Nếu không tất toán toàn bộ dư nợ tối thiểu trước ngày đến hạn, phí chậm trả và lãi quá hạn sẽ được tính theo biểu phí thỏa thuận.',
        actionable_angle: 'Lịch chốt sao kê hàng tháng và công thức tính chi phí chuyển đổi trả góp.',
      },
    },
    sources: [
      'Thông tư 39/2016/TT-NHNN quy định về hoạt động cho vay của tổ chức tín dụng',
      'Thông tư 03/2013/TT-NHNN quy định về hoạt động thông tin tín dụng',
      'Điều khoản và điều kiện dịch vụ Ví Trả Sau hợp tác giữa MoMo và TPBank',
    ],
  },

  financial_consumer_loan: {
    hub: 'Financial Hub',
    schema_type: 'LoanOrCredit',
    schema_category: 'https://schema.org/LoanOrCredit',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói vay tín chấp hoặc thế chấp tiêu dùng.' },
      { field: 'provider', desc: 'Công ty tài chính hoặc ngân hàng thương mại được NHNN cấp phép.' },
      { field: 'annualPercentageRate', desc: 'Lãi suất vay danh nghĩa và lãi suất thực tế (%/năm).' },
      { field: 'loanTerm', desc: 'Kỳ hạn vay tối thiểu và tối đa (tháng).' },
      { field: 'amount', desc: 'Hạn mức khoản vay tối đa.' },
    ],
    direct_answer_text:
      'Vay tiêu dùng là hình thức cấp vốn tín dụng từ ngân hàng hoặc công ty tài chính được Ngân hàng Nhà nước cấp phép, giải quyết nhu cầu chi tiêu cấp bách. Khách hàng có thể chọn vay tín chấp theo lương hoặc vay thế chấp tài sản với lãi suất minh bạch.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'LoanOrCredit',
      name: 'Vay Tiêu Dùng Cá Nhân',
      provider: {
        '@type': 'FinancialService',
        name: 'Công ty Tài chính Cổ phần Điện lực (EVN Finance)',
      },
      loanTerm: {
        '@type': 'QuantitativeValue',
        minValue: 6,
        maxValue: 36,
        unitText: 'tháng',
      },
      amount: {
        '@type': 'MonetaryAmount',
        currency: 'VND',
        value: 50000000,
      },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế cho vay tiêu dùng theo Thông tư 43/2016/TT-NHNN',
        summary: 'Phân biệt rõ ràng giữa cho vay ngân hàng và cho vay của công ty tài chính.',
        detail:
          'Hoạt động cho vay tiêu dùng của các công ty tài chính chịu sự điều chỉnh của Thông tư 43/2016/TT-NHNN và Thông tư 18/2019/TT-NHNN, quy định trần lãi suất, tỷ lệ giải ngân trực tiếp cho khách hàng và phương thức đòi nợ đúng chuẩn mực pháp lý.',
        actionable_angle: 'Bảng đối chiếu điều kiện vay tín chấp giữa ngân hàng thương mại và công ty tài chính.',
      },
      trust: {
        title: 'Minh bạch hợp đồng tín dụng & Cảnh báo bẫy tín dụng đen',
        summary: 'Chỉ giải ngân qua các đối tác tài chính có giấy phép hoạt động hợp pháp.',
        detail:
          'Người vay được cung cấp đầy đủ bảng tính lịch trả nợ, lãi suất tính theo dư nợ giảm dần và bản sao hợp đồng tín dụng điện tử. Tuyệt đối không giao dịch với các ứng dụng vay tiền nhanh không có giấy phép của NHNN.',
        actionable_angle: 'Checklist 6 dấu hiệu nhận biết bẫy tín dụng đen trực tuyến và phí ẩn giả mạo giải ngân.',
      },
      high_intent: {
        title: 'Công cụ tính lãi theo dư nợ giảm dần vs. Dư nợ ban đầu',
        summary: 'Làm rõ sự chênh lệch lớn giữa lãi suất phẳng và lãi suất thực tế.',
        detail:
          'Cung cấp bảng mô phỏng dòng tiền trả góp hàng tháng (gốc + lãi) theo phương pháp dư nợ giảm dần, chỉ rõ mức phí phạt trả nợ trước hạn (1-5% số tiền trả trước hạn) và phí phạt quá hạn tối đa 150% lãi suất trong hạn.',
        actionable_angle: 'Bảng so sánh chi phí vay thực tế giữa kỳ hạn 12 tháng, 24 tháng và 36 tháng.',
      },
    },
    sources: [
      'Luật Các tổ chức tín dụng số 32/2024/QH15',
      'Thông tư 39/2016/TT-NHNN quy định về hoạt động cho vay của TCTD',
      'Thông tư 43/2016/TT-NHNN và Thông tư 18/2019/TT-NHNN về cho vay tiêu dùng của công ty tài chính',
    ],
  },

  financial_credit_line: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói hạn mức tín dụng hoặc dịch vụ quản lý dư nợ.' },
      { field: 'provider', desc: 'Ngân hàng thương mại cấp hạn mức.' },
      { field: 'annualPercentageRate', desc: 'Lãi suất trong hạn và lãi suất quá hạn.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Quy định thời hạn duy trì hạn mức và phí quản lý.' },
    ],
    direct_answer_text:
      'Hạn mức tín dụng và dư nợ cá nhân phản ánh số tiền khách hàng được phép chi tiêu vượt số dư hoặc đang nợ tổ chức tín dụng. Người dùng chỉ trả lãi trên số tiền và số ngày thực tế sử dụng vốn, tuân thủ nghiêm ngặt quy chế kiểm soát nợ của NHNN.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Hạn Mức Thấu Chi & Tín Dụng Cá Nhân',
      provider: {
        '@type': 'BankOrCreditUnion',
        name: 'Ngân hàng TMCP Bản Việt (BVBank)',
      },
      feesAndCommissionsSpecification: 'Lãi tính trên dư nợ thực tế và số ngày sử dụng vốn theo ngày',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Cơ chế tính lãi thấu chi trên dư nợ thực tế hàng ngày',
        summary: 'Tuân thủ Thông tư 39/2016/TT-NHNN về phương pháp tính lãi suất tiền vay.',
        detail:
          'Tiền lãi thấu chi được tính theo công thức: Dư nợ thực tế cuối ngày x Lãi suất năm / 365 x Số ngày duy trì dư nợ. Khách hàng không bị tính lãi trên phần hạn mức chưa giải ngân.',
        actionable_angle: 'Bảng công thức tính lãi vay thấu chi và đối chiếu thời điểm tất toán tránh phát sinh lãi ngày mới.',
      },
      trust: {
        title: 'Kiểm soát tỷ lệ sử dụng hạn mức & Phòng ngừa nợ xấu CIC',
        summary: 'Khuyến nghị duy trì tỷ lệ sử dụng hạn mức dưới ngưỡng an toàn 30%.',
        detail:
          'Duy trì tỷ lệ nợ trên hạn mức quá cao hoặc chậm thanh toán gốc lãi quá 10 ngày sẽ kích hoạt cảnh báo nợ nhóm 2 và chuyển nhóm nợ xấu trên hệ thống CIC Quốc gia theo Thông tư 11/2021/TT-NHNN.',
        actionable_angle: 'Hướng dẫn kích hoạt tính năng trích nợ tự động chống quên lịch thanh toán định kỳ.',
      },
      high_intent: {
        title: 'Phân bổ dòng tiền trả nợ: Ưu tiên nợ lãi suất cao vs. Nợ sắp quá hạn',
        summary: 'Chiến lược tối ưu hóa thứ tự thanh toán giảm thiểu tối đa chi phí lãi phát sinh.',
        detail:
          'Cung cấp phương pháp thanh toán nợ tối ưu theo thứ tự ưu tiên: Phí phát sinh -> Lãi quá hạn -> Lãi trong hạn -> Nợ gốc quá hạn -> Nợ gốc trong hạn theo đúng quy định tại Điều 12 Thông tư 39/2016/TT-NHNN.',
        actionable_angle: 'Bảng lập kế hoạch thanh toán dư nợ theo phương pháp quả cầu tuyết (Snowball) và tuyết lở (Avalanche).',
      },
    },
    sources: [
      'Thông tư 39/2016/TT-NHNN quy định về hoạt động cho vay của TCTD',
      'Thông tư 11/2021/TT-NHNN quy định về phân loại tài sản có, trích lập dự phòng rủi ro của TCTD',
    ],
  },

  financial_card_payment: {
    hub: 'Financial Hub',
    schema_type: 'PaymentService',
    schema_category: 'https://schema.org/PaymentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên loại thẻ thanh toán hoặc phương thức chuyển tiền.' },
      { field: 'provider', desc: 'Ngân hàng phát hành hoặc tổ chức chuyển mạch thẻ (NAPAS, Visa, Mastercard).' },
      { field: 'feesAndCommissionsSpecification', desc: 'Biểu phí thường niên, phí giao dịch ngoại tệ và phí rút tiền mặt.' },
      { field: 'areaServed', desc: 'Phạm vi chấp nhận thẻ (Nội địa hoặc Quốc tế).' },
    ],
    direct_answer_text:
      'Thẻ thanh toán và dịch vụ chuyển khoản là phương tiện giao dịch không dùng tiền mặt do ngân hàng và tổ chức tài chính được NHNN cấp phép phát hành. Người dùng có thể chi tiêu qua thẻ ghi nợ, thẻ tín dụng, quét mã VietQR hoặc chuyển tiền liên ngân hàng 24/7 tức thì.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'PaymentService',
      name: 'Dịch Vụ Thanh Toán & Thẻ Ngân Hàng',
      provider: {
        '@type': 'BankOrCreditUnion',
        name: 'Hệ thống Ngân hàng Thành viên NAPAS & Quốc tế',
      },
      serviceType: 'Thanh toán thẻ và Chuyển tiền liên ngân hàng 24/7',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định phát hành thẻ & Chuyển khoản liên ngân hàng NAPAS',
        summary: 'Tuân thủ Thông tư 19/2016/TT-NHNN và Thông tư 26/2017/TT-NHNN về hoạt động thẻ ngân hàng.',
        detail:
          'Quy chuẩn kỹ thuật thẻ chip tiếp xúc và không tiếp xúc theo tiêu chuẩn VCCS (nội địa) và EMV (quốc tế), đảm bảo tính toàn vẹn dữ liệu giao dịch và ngăn chặn sao chép thông tin thẻ trái phép.',
        actionable_angle: 'Bảng phân biệt quyền lợi, cơ chế hoạt động và biểu phí giữa thẻ ghi nợ (Debit) và thẻ tín dụng (Credit).',
      },
      trust: {
        title: 'Bảo mật 3D-Secure đa lớp & Khóa thẻ khẩn cấp 1 chạm',
        summary: 'Bảo vệ thông tin số thẻ CVV/CVC và chống gian lận thanh toán xuyên biên giới.',
        detail:
          'Mọi giao dịch thanh toán trực tuyến đều được mã hóa bằng chuẩn 3D-Secure 2.0 (OTP/Biometric). Người dùng được chủ động bật/tắt tính năng thanh toán trực tuyến và khóa thẻ ngay tức thì trên ứng dụng khi có nghi vấn lộ thẻ.',
        actionable_angle: 'Checklist 5 nguyên tắc bảo vệ mặt sau thẻ (mã CVV) và kích hoạt cảnh báo biến động số dư.',
      },
      high_intent: {
        title: 'Biểu phí giao dịch: Phí chuyển đổi ngoại tệ, phí rút tiền mặt & Phí thường niên',
        summary: 'Bóc tách các loại phí tiềm ẩn khi quẹt thẻ trong nước và quốc tế.',
        detail:
          'Cung cấp bảng so sánh chi tiết mức phí chuyển đổi ngoại tệ (từ 1.5% đến 3.5%), phí xử lý giao dịch quốc tế và cảnh báo phí rút tiền mặt tại ATM bằng thẻ tín dụng (thường là 4% số tiền rút, tối thiểu 50.000 - 100.000 VNĐ).',
        actionable_angle: 'Bảng so sánh hạn mức chuyển khoản VietQR và phí thường niên thẻ của các ngân hàng top đầu.',
      },
    },
    sources: [
      'Thông tư 19/2016/TT-NHNN quy định về hoạt động thẻ ngân hàng (sửa đổi, bổ sung)',
      'Quyết định 2345/QĐ-NHNN về triển khai giải pháp an toàn, bảo mật trong thanh toán trực tuyến',
      'Tiêu chuẩn kỹ thuật thẻ chip nội địa VCCS của NAPAS',
    ],
  },

  financial_investment: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên sản phẩm đầu tư (Cổ phiếu, Trái phiếu, Chứng chỉ quỹ ETF).' },
      { field: 'provider', desc: 'Công ty chứng khoán hoặc Công ty quản lý quỹ được UBCKNN cấp phép.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Biểu phí giao dịch chứng khoán, thuế chuyển nhượng và phí quản lý quỹ.' },
    ],
    direct_answer_text:
      'Đầu tư chứng khoán và chứng chỉ quỹ là hoạt động góp vốn vào doanh nghiệp niêm yết hoặc quỹ đại chúng được Ủy ban Chứng khoán Nhà nước cấp phép. Tài sản chứng khoán và tiền của nhà đầu tư được quản lý tách bạch tại VSDC, khớp lệnh minh bạch qua sàn.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Dịch Vụ Giao Dịch Chứng Khoán Trực Tuyến CVS',
      provider: {
        '@type': 'FinancialService',
        name: 'Công ty Cổ phần Chứng khoán CV (CVS)',
        url: 'https://cvs.vn',
      },
      feesAndCommissionsSpecification:
        'Phí giao dịch khớp lệnh theo biểu phí CVS; Thuế TNCN chuyển nhượng chứng khoán 0.1% giá trị bán',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Khung pháp lý UBCKNN & Quản lý tài sản tách bạch tại VSDC',
        summary: 'Chứng khoán không phải tiền gửi và không thuộc phạm vi bảo hiểm tiền gửi BHTGVN.',
        detail:
          'Thị trường chứng khoán vận hành theo Luật Chứng khoán số 54/2019/QH14. Toàn bộ cổ phiếu, trái phiếu và chứng chỉ quỹ được đăng ký, lưu ký tập trung tại Tổng công ty Lưu ký và Bù trừ Chứng khoán Việt Nam (VSDC). Tài sản tiền và chứng khoán của khách hàng được quản lý tách biệt hoàn toàn khỏi tài sản của công ty chứng khoán theo Thông tư 121/2020/TT-BTC.',
        actionable_angle: 'Quy trình mở tài khoản chứng khoán eKYC tại CVS và đối soát mã sở hữu tài sản tại VSDC.',
      },
      trust: {
        title: 'Cơ chế tách bạch tiền gửi đầu tư & Cảnh báo rủi ro biến động thị trường',
        summary: 'Khẳng định nguyên tắc thị trường: Lợi nhuận đi kèm rủi ro biến động giá vốn.',
        detail:
          'Đầu tư chứng khoán không có cam kết hoàn vốn cố định. Nhà đầu tư được bảo vệ thông qua nghĩa vụ công bố thông tin minh bạch định kỳ và bất thường của tổ chức niêm yết theo quy định tại Thông tư 96/2020/TT-BTC.',
        actionable_angle: 'Checklist 5 bước đọc báo cáo tài chính đã kiểm toán và kiểm tra tình trạng pháp lý mã cổ phiếu.',
      },
      high_intent: {
        title: 'Biểu phí giao dịch, thuế bán 0.1% & Chu kỳ thanh toán T+2 của VSDC',
        summary: 'Minh bạch chu kỳ thanh toán bù trừ và toàn bộ chi phí mua bán chứng khoán.',
        detail:
          'Làm rõ chu kỳ thanh toán giao dịch cổ phiếu là T+2 (cổ phiếu về tài khoản vào 13h00 ngày T+2), thuế thu nhập cá nhân khi chuyển nhượng cổ phiếu là 0.1% trên tổng giá trị bán, và thuế thu nhập từ cổ tức tiền mặt là 5% theo Luật Thuế TNCN.',
        actionable_angle: 'Bảng tính thuế phí chi tiết trên một lệnh giao dịch mua/bán và so sánh phí quản lý chứng chỉ quỹ mở.',
      },
    },
    sources: [
      'Luật Chứng khoán số 54/2019/QH14',
      'Thông tư 121/2020/TT-BTC quy định về hoạt động của công ty chứng khoán',
      'Thông tư 96/2020/TT-BTC hướng dẫn công bố thông tin trên thị trường chứng khoán',
      'Thông tư 111/2013/TT-BTC hướng dẫn thực hiện Luật Thuế TNCN về thuế chuyển nhượng chứng khoán',
    ],
  },

  financial_gold_fx: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên kim loại quý hoặc cặp tiền tệ quy đổi.' },
      { field: 'provider', desc: 'Doanh nghiệp kinh doanh vàng hoặc Ngân hàng thương mại được cấp phép.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Chênh lệch giá mua vào - bán ra (Spread) và phí đổi ngoại tệ.' },
    ],
    direct_answer_text:
      'Giá vàng và tỷ giá ngoại tệ phản ánh giá trị quy đổi của kim loại quý và đồng tiền quốc tế dưới sự quản lý của Ngân hàng Nhà nước. Người dân được cập nhật dữ liệu tỷ giá và giao dịch tại các tổ chức tín dụng, doanh nghiệp kinh doanh vàng được cấp phép.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Bảng Giá Vàng & Tỷ Giá Ngoại Tệ Trực Tuyến',
      provider: {
        '@type': 'BankOrCreditUnion',
        name: 'Hệ thống Ngân hàng Thương mại & Đơn vị Kinh doanh Vàng được cấp phép',
      },
      feesAndCommissionsSpecification: 'Giá niêm yết theo giá mua vào - bán ra thời gian thực',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định độc quyền vàng miếng SJC theo Nghị định 24/2012/NĐ-CP',
        summary: 'Khung pháp lý về hoạt động kinh doanh vàng và quản lý ngoại hối của NHNN.',
        detail:
          'Ngân hàng Nhà nước độc quyền sản xuất vàng miếng và quản lý chặt chẽ hoạt động kinh doanh mua, bán vàng miếng theo Nghị định 24/2012/NĐ-CP. Giao dịch ngoại tệ tiền mặt phải có chứng từ chứng minh mục đích hợp pháp theo Pháp lệnh Ngoại hối.',
        actionable_angle: 'Bảng tra cứu danh sách tổ chức được NHNN cấp giấy phép kinh doanh mua bán vàng miếng.',
      },
      trust: {
        title: 'Chênh lệch giá vàng nội địa - thế giới & Tiêu chuẩn tuổi vàng 99.99%',
        summary: 'Minh bạch chất lượng vàng trang sức, vàng nhẫn trơn và vàng miếng SJC.',
        detail:
          'Cảnh báo chênh lệch lớn giữa giá vàng SJC trong nước và giá vàng thế giới quy đổi, cũng như khoảng cách giữa giá mua vào và bán ra (spread) tại các thời điểm thị trường biến động mạnh.',
        actionable_angle: 'Quy chuẩn đọc dấu kiểm định chất lượng, thương hiệu vàng và bảo quản hóa đơn gốc khi giao dịch.',
      },
      high_intent: {
        title: 'Công cụ quy đổi tỷ giá ngoại tệ & Bảng so sánh spread các ngân hàng',
        summary: 'Cập nhật tỷ giá mua tiền mặt, mua chuyển khoản và bán ra của các đồng tiền phổ biến.',
        detail:
          'Cung cấp công cụ tính toán quy đổi tức thì giữa VNĐ và các đồng ngoại tệ mạnh (USD, EUR, JPY, GBP, KRW) dựa trên tỷ giá trung tâm của NHNN và tỷ giá niêm yết thương mại.',
        actionable_angle: 'Bảng đối chiếu chênh lệch tỷ giá mua chuyển khoản và tiền mặt giữa 5 ngân hàng lớn.',
      },
    },
    sources: [
      'Nghị định 24/2012/NĐ-CP về quản lý hoạt động kinh doanh vàng',
      'Pháp lệnh Ngoại hối số 28/2005/PL-UBTVQH11 và Pháp lệnh sửa đổi số 07/2013/UBTVQH13',
      'Thông tư 02/2021/TT-NHNN hướng dẫn về giao dịch ngoại tệ trên thị trường ngoại tệ',
    ],
  },

  financial_credit_score: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên báo cáo thông tin tín dụng cá nhân.' },
      { field: 'provider', desc: 'Trung tâm Thông tin Tín dụng Quốc gia Việt Nam (CIC).' },
      { field: 'description', desc: 'Thang điểm tín dụng và phân loại nhóm nợ.' },
    ],
    direct_answer_text:
      'Điểm tín dụng cá nhân và báo cáo CIC là chỉ số đo lường độ uy tín tài chính của cá nhân do Trung tâm Thông tin Tín dụng Quốc gia quản lý. Điểm số này quyết định trực tiếp khả năng duyệt vay vốn, hạn mức cấp thẻ và lãi suất tại các ngân hàng.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Báo Cáo Điểm Tín Dụng Cá Nhân CIC',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Trung tâm Thông tin Tín dụng Quốc gia Việt Nam (CIC)',
        url: 'https://cic.gov.vn',
      },
      description: 'Tra cứu điểm xếp hạng tín dụng cá nhân và lịch sử quan hệ tín dụng theo dữ liệu NHNN',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định phân loại nợ 5 nhóm theo Thông tư 11/2021/TT-NHNN',
        summary: 'Khung pháp lý về thu thập và xử lý thông tin tín dụng khách hàng của NHNN.',
        detail:
          'CIC phân loại nợ thành 5 nhóm: Nhóm 1 (Đủ tiêu chuẩn), Nhóm 2 (Cần chú ý, quá hạn 10-90 ngày), Nhóm 3 (Dưới tiêu chuẩn), Nhóm 4 (Nghi ngờ), Nhóm 5 (Có khả năng mất vốn, quá hạn trên 360 ngày). Nợ từ nhóm 3 đến 5 được định nghĩa là nợ xấu.',
        actionable_angle: 'Bảng chi tiết tiêu chí phân loại 5 nhóm nợ và thời gian lưu vết thông tin nợ trên hệ thống CIC.',
      },
      trust: {
        title: 'Quy trình xóa vết nợ xấu & Cảnh báo dịch vụ xóa nợ CIC lừa đảo',
        summary: 'Dữ liệu CIC là cơ sở dữ liệu quốc gia bất khả xâm phạm, không có dịch vụ nào can thiệp được ngoài việc tất toán nợ.',
        detail:
          'Lịch sử nợ xấu nhóm 2 sẽ tự động xóa sau 12 tháng kể từ ngày tất toán toàn bộ dư nợ; nợ xấu nhóm 3-5 được lưu giữ trong thời gian tối đa 5 năm theo quy định tại Điều 11 Thông tư 03/2013/TT-NHNN. Mọi lời mời chào xóa nợ xấu lấy phí đều là hành vi lừa đảo chiếm đoạt tài sản.',
        actionable_angle: 'Quy trình 3 bước gửi đơn đề nghị đính chính thông tin khi phát hiện dữ liệu tín dụng CIC bị sai lệch.',
      },
      high_intent: {
        title: 'Hướng dẫn tự tra cứu báo cáo tín dụng cá nhân miễn phí trên CIC',
        summary: 'Cách kiểm tra điểm tín dụng và lịch sử vay nợ chính chủ định kỳ 1 năm 1 lần.',
        detail:
          'Mỗi công dân được quyền khai thác 1 báo cáo tín dụng cá nhân miễn phí mỗi năm trên Cổng thông tin CIC (cic.gov.vn) hoặc ứng dụng CIC Connect để chủ động kiểm tra xem có bị mạo danh mở thẻ hoặc đứng tên khoản vay hay không.',
        actionable_angle: 'Bộ tiêu chí 4 yếu tố giúp cải thiện điểm tín dụng từ Hạng B lên Hạng A trong vòng 6 tháng.',
      },
    },
    sources: [
      'Thông tư 03/2013/TT-NHNN quy định về hoạt động thông tin tín dụng của Ngân hàng Nhà nước',
      'Thông tư 11/2021/TT-NHNN về phân loại tài sản có, mức trích lập dự phòng rủi ro của TCTD',
      'Cổng thông tin tín dụng quốc gia CIC Việt Nam (cic.gov.vn)',
    ],
  },

  tax_payroll: {
    hub: 'Financial Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên thủ tục thuế hoặc tiện ích tính lương, phí trước bạ.' },
      { field: 'provider', desc: 'Cơ quan Thuế trực thuộc Tổng cục Thuế hoặc Cổng Dịch vụ công Quốc gia.' },
      { field: 'serviceType', desc: 'Tra cứu nghĩa vụ thuế, quyết toán thuế TNCN hoặc tính lệ phí trước bạ tài sản.' },
    ],
    direct_answer_text:
      'Thuế thu nhập cá nhân và lệ phí trước bạ là nghĩa vụ tài chính công dân nộp ngân sách theo Luật Thuế TNCN và Nghị định 10/2022/NĐ-CP. Công dân được giảm trừ gia cảnh 11 triệu đồng cho bản thân, 4,4 triệu đồng cho người phụ thuộc, hoặc nộp lệ phí trước bạ theo quy định tài sản.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Dịch Vụ Tra Cứu Nghĩa Vụ Thuế & Lương Cá Nhân',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Tổng cục Thuế - Bộ Tài chính',
        url: 'https://www.gdt.gov.vn',
      },
      serviceType: 'Tra cứu mã số thuế, quyết toán thuế TNCN và tính lệ phí trước bạ',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Biểu thuế TNCN lũy tiến từng phần & Khung lệ phí trước bạ tài sản',
        summary: 'Căn cứ Luật Thuế TNCN và Nghị định 10/2022/NĐ-CP về lệ phí trước bạ.',
        detail:
          'Thuế TNCN từ tiền lương áp dụng 7 bậc lũy tiến từ 5% đến 35% sau khi trừ các khoản đóng bảo hiểm bắt buộc và giảm trừ gia cảnh. Lệ phí trước bạ ô tô, xe máy được tính theo tỷ lệ phần trăm (ô tô con từ 10-12%, xe máy 2-5%) nhân với giá trị tính lệ phí trước bạ do Bộ Tài chính ban hành.',
        actionable_angle: 'Bảng đối chiếu 7 bậc thuế TNCN và bảng tỷ lệ thu lệ phí trước bạ theo từng nhóm tài sản.',
      },
      trust: {
        title: 'Tra cứu Mã số thuế (MST) & Đối soát nghĩa vụ nộp thuế chính thức',
        summary: 'Kết nối dữ liệu trực tiếp với hệ thống eTax Mobile và Cổng Dịch vụ công Quốc gia.',
        detail:
          'Tra cứu mã số thuế cá nhân và nghĩa vụ thuế tồn đọng được chuẩn hóa dựa trên số Căn cước công dân gắn chip theo Đề án 06, ngăn chặn việc bị doanh nghiệp mạo danh kê khai khống thu nhập để trốn thuế.',
        actionable_angle: 'Quy trình kiểm tra hồ sơ quyết toán thuế TNCN trực tuyến và xử lý hoàn thuế thừa về tài khoản.',
      },
      high_intent: {
        title: 'Công cụ chuyển đổi lương Gross sang Net & Dự toán lệ phí trước bạ xe',
        summary: 'Minh bạch công thức khấu trừ BHXH, BHYT, BHTN và các khoản thuế phải nộp.',
        detail:
          'Bóc tách chi tiết các khoản trừ lương gồm BHXH 8%, BHYT 1.5%, BHTN 1% trên mức lương đóng bảo hiểm (áp dụng mức trần lương cơ sở theo luật định), giúp người lao động nắm rõ thu nhập thực nhận.',
        actionable_angle: 'Bảng so sánh chi phí đóng thuế giữa người có 1 người phụ thuộc và người không có người phụ thuộc.',
      },
    },
    sources: [
      'Luật Thuế Thu nhập cá nhân số 04/2007/QH12 (sửa đổi, bổ sung)',
      'Nghị quyết 954/2020/UBTVQH14 về điều chỉnh mức giảm trừ gia cảnh thuế TNCN',
      'Nghị định 10/2022/NĐ-CP quy định về lệ phí trước bạ',
      'Thông tư 111/2013/TT-BTC hướng dẫn thực hiện Luật Thuế TNCN',
    ],
  },

  macro_knowledge: {
    hub: 'Financial Hub',
    schema_type: 'Article',
    schema_category: 'https://schema.org/Article',
    mandatory_fields: [
      { field: 'headline', desc: 'Tiêu đề bài viết kiến thức kinh tế và quản trị tài chính.' },
      { field: 'description', desc: 'Tóm tắt khái niệm kinh tế vĩ mô hoặc nguyên lý tài chính cá nhân.' },
      { field: 'author', desc: 'Tên tổ chức biên soạn nội dung chuyên môn.' },
    ],
    direct_answer_text:
      'Kinh tế vĩ mô và tài chính cá nhân là hệ thống kiến thức về GDP, lạm phát, dòng tiền và nguyên lý lãi kép. Nắm vững bản chất tích lũy tài sản và kiểm soát tiêu sản giúp người đọc xây dựng kế hoạch quản trị dòng tiền, lập quỹ dự phòng và đạt tự do tài chính.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: 'Kiến Thức Tài Chính Cá Nhân & Kinh Tế Vĩ Mô',
      description: 'Phân tích các nguyên lý kinh tế học, công thức lãi kép và chiến lược quản lý dòng tiền cá nhân',
      author: {
        '@type': 'Organization',
        name: 'Nền tảng Web MoMo',
        url: 'https://www.momo.vn',
      },
      inLanguage: 'vi-VN',
    },
    pillars: {
      expertise: {
        title: 'Chỉ số kinh tế vĩ mô & Chu kỳ kinh tế của Tổng cục Thống kê',
        summary: 'Cơ sở định nghĩa học thuật chuẩn mực về GDP, CPI, lạm phát và chu kỳ tiền tệ.',
        detail:
          'Giải thích cơ chế vận hành của chính sách tiền tệ và tài khóa: Tác động của lạm phát làm xói mòn sức mua của tiền mặt và tầm quan trọng của việc duy trì tỷ suất sinh lời thực dương sau khi trừ đi tỷ lệ lạm phát hàng năm.',
        actionable_angle: 'Bảng dữ liệu tăng trưởng GDP và chỉ số giá tiêu dùng CPI qua các năm theo báo cáo GSO.',
      },
      trust: {
        title: 'Nguyên lý tích lũy tài sản thực vs. Bẫy chi tiêu tiêu sản',
        summary: 'Phân biệt rõ ràng giữa tài sản sinh dòng tiền và tiêu sản khấu hao giá trị.',
        detail:
          'Áp dụng định nghĩa tài chính chuẩn mực: Tài sản bỏ tiền vào túi bạn thông qua lợi tức hoặc gia tăng vốn, tiêu sản lấy tiền ra khỏi túi thông qua chi phí duy trì và khấu hao giá trị theo thời gian.',
        actionable_angle: 'Ma trận đánh giá danh mục tài sản cá nhân và tiêu chuẩn quy mô quỹ dự phòng khẩn cấp 3-6 tháng chi phí sinh hoạt.',
      },
      high_intent: {
        title: 'Mô hình quy tắc 50/30/20 & Công thức toán học lãi kép',
        summary: 'Ứng dụng công thức giá trị tương lai FV = PV * (1 + r)^n trong lập kế hoạch FIRE.',
        detail:
          'Minh họa sức mạnh của lãi kép và thời gian tích lũy đối với mục tiêu độc lập tài chính, kèm hướng dẫn phân bổ thu nhập theo quy tắc 50% nhu cầu thiết yếu, 30% sở thích cá nhân và 20% cho tiết kiệm, đầu tư.',
        actionable_angle: 'Bảng tính mô phỏng kết quả tài sản sau 10, 20, 30 năm khi tích lũy định kỳ hàng tháng với các mức lãi suất kỳ vọng khác nhau.',
      },
    },
    sources: [
      'Số liệu thống kê kinh tế vĩ mô của Tổng cục Thống kê Việt Nam (GSO)',
      'Nguyên lý Kinh tế học (Principles of Economics) - N. Gregory Mankiw',
      'Các báo cáo phân tích kinh tế định kỳ của Viện Nghiên cứu Kinh tế và Chính sách (VEPR)',
    ],
  },

  vehicle_traffic_fines: {
    hub: 'Vehicle Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên dịch vụ tra cứu phạt nguội giao thông.' },
      { field: 'provider', desc: 'Cục Cảnh sát Giao thông - Bộ Công an.' },
      { field: 'serviceType', desc: 'Tra cứu lỗi vi phạm giao thông và phương thức nộp phạt trực tuyến.' },
    ],
    direct_answer_text:
      'Phạt nguội là hình thức xử lý vi phạm an toàn giao thông đường bộ được phát hiện qua hệ thống camera giám sát của lực lượng Cảnh sát Giao thông. Dữ liệu vi phạm cập nhật chính thức trên cổng csgt.vn để chủ xe tra cứu và nộp phạt trực tuyến qua Cổng Dịch vụ công Quốc gia.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Tra Cứu Phạt Nguội Giao Thông Đường Bộ',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Cục Cảnh sát Giao thông - Bộ Công an',
        url: 'https://www.csgt.vn',
      },
      serviceType: 'Tra cứu lỗi vi phạm giao thông qua camera giám sát và nộp phạt trực tuyến',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Khung pháp lý xử phạt theo Nghị định 168/2024/NĐ-CP',
        summary: 'Căn cứ quy định mức phạt tiền, trừ điểm giấy phép lái xe và tạm giữ phương tiện.',
        detail:
          'Nghị định 168/2024/NĐ-CP quy định chi tiết mức xử phạt vi phạm hành chính trật tự ATGT đường bộ và cơ chế trừ điểm, phục hồi điểm giấy phép lái xe đối với các lỗi vượt đèn đỏ, chạy quá tốc độ, đi sai làn đường.',
        actionable_angle: 'Bảng tra cứu khung tiền phạt và số điểm bị trừ trên giấy phép lái xe đối với ô tô và xe máy theo Nghị định 168/2024/NĐ-CP.',
      },
      trust: {
        title: 'Nguồn dữ liệu đối soát Cục CSGT (csgt.vn) & Cảnh báo lừa đảo phạt nguội',
        summary: 'Cơ quan công an không gửi thông báo phạt nguội qua điện thoại hoặc yêu cầu chuyển khoản cá nhân.',
        detail:
          'Thông báo vi phạm được gửi bằng văn bản giấy tới chủ xe hoặc cập nhật trực tiếp trên hệ thống csgt.vn. Tuyệt đối cảnh giác với các cuộc gọi mạo danh cán bộ CSGT yêu cầu chuyển tiền nộp phạt vào tài khoản cá nhân.',
        actionable_angle: 'Quy trình 4 bước xác thực thông báo vi phạm chính thức và quy chuẩn nộp phạt qua Cổng Dịch vụ công Quốc gia.',
      },
      high_intent: {
        title: 'Thời hạn đóng phạt nguội & Nguy cơ bị từ chối đăng kiểm phương tiện',
        summary: 'Cơ chế phối hợp dữ liệu giữa Cục CSGT và Cục Đăng kiểm Việt Nam.',
        detail:
          'Phương tiện chưa hoàn thành nghĩa vụ nộp phạt nguội sẽ bị đưa vào danh sách cảnh báo trên hệ thống kiểm định và bị các trung tâm đăng kiểm từ chối kiểm định theo quy định tại Thông tư 16/2021/TT-BGTVT.',
        actionable_angle: 'Hướng dẫn nộp phạt trực tuyến qua Cổng Dịch vụ công Quốc gia để gỡ cảnh báo đăng kiểm trong 24-48 giờ.',
      },
    },
    sources: [
      'Nghị định 168/2024/NĐ-CP về xử phạt vi phạm hành chính trật tự ATGT đường bộ; trừ điểm GPLX',
      'Cổng thông tin điện tử Cục Cảnh sát Giao thông (csgt.vn)',
    ],
  },

  driver_license: {
    hub: 'Vehicle Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên thủ tục đào tạo, sát hạch GPLX hoặc đăng kiểm phương tiện.' },
      { field: 'provider', desc: 'Cục Đường bộ Việt Nam hoặc Cục Đăng kiểm Việt Nam thuộc Bộ GTVT.' },
      { field: 'serviceType', desc: 'Sát hạch, cấp đổi GPLX và kiểm định xe cơ giới.' },
    ],
    direct_answer_text:
      'Giấy phép lái xe và đăng kiểm là chứng chỉ bắt buộc chứng minh năng lực điều khiển phương tiện và tiêu chuẩn an toàn kỹ thuật xe cơ giới. Quy trình sát hạch GPLX gồm lý thuyết, 120 tình huống mô phỏng và thực hành sa hình theo quy định chặt chẽ của Bộ GTVT.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Dịch Vụ Sát Hạch GPLX & Đăng Kiểm Xe Cơ Giới',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Cục Đường bộ Việt Nam & Cục Đăng kiểm Việt Nam - Bộ GTVT',
        url: 'https://drvn.gov.vn',
      },
      serviceType: 'Sát hạch, cấp đổi giấy phép lái xe và kiểm định an toàn phương tiện cơ giới',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn sát hạch 600 câu lý thuyết & 120 tình huống mô phỏng theo Thông tư 04/2022/TT-BGTVT',
        summary: 'Tiêu chuẩn kiểm tra kiến thức luật giao thông và phản xạ xử lý nguy cơ tai nạn.',
        detail:
          'Học viên thi sát hạch lái xe ô tô phải vượt qua phần thi lý thuyết (bao gồm câu điểm liệt), phần mềm mô phỏng 120 tình huống giao thông nguy hiểm và thực hành lái xe trên cabin mô phỏng cùng thiết bị DAT.',
        actionable_angle: 'Bộ quy tắc nhận biết thời điểm ấn Space trong 120 tình huống mô phỏng để đạt điểm tối đa (5 điểm).',
      },
      trust: {
        title: 'Tra cứu GPLX thật/giả trên gplx.gov.vn & Tích hợp VNeID',
        summary: 'Hệ thống cơ sở dữ liệu GPLX toàn quốc trực thuộc Cục Đường bộ Việt Nam.',
        detail:
          'Hướng dẫn người dân tự tra cứu số seri GPLX trên hệ thống chính thức của Bộ GTVT để phát hiện bằng giả. GPLX hợp lệ được tích hợp vào tài khoản định danh điện tử VNeID mức 2 theo quy định mới.',
        actionable_angle: 'Quy trình cấp đổi GPLX trực tuyến mức độ 4 nhận kết quả tại nhà qua Cổng Dịch vụ công Quốc gia.',
      },
      high_intent: {
        title: 'Chu kỳ đăng kiểm xe cơ giới & Quy trình đặt lịch hẹn kiểm định',
        summary: 'Cập nhật chu kỳ kiểm định phương tiện cơ giới đường bộ theo Thông tư 08/2023/TT-BGTVT.',
        detail:
          'Làm rõ quy định miễn kiểm định lần đầu cho ô tô mới chưa qua sử dụng và giãn chu kỳ đăng kiểm đối với ô tô con không kinh doanh vận tải lên đến 36 tháng, 24 tháng hoặc 12 tháng tùy theo năm sản xuất.',
        actionable_angle: 'Bảng tra cứu chu kỳ đăng kiểm chi tiết theo từng loại xe và hướng dẫn đặt lịch hẹn trực tuyến tránh xếp hàng.',
      },
    },
    sources: [
      'Thông tư 12/2017/TT-BGTVT quy định về đào tạo, sát hạch, cấp giấy phép lái xe cơ giới đường bộ',
      'Thông tư 04/2022/TT-BGTVT sửa đổi, bổ sung Thông tư 12/2017/TT-BGTVT',
      'Thông tư 16/2021/TT-BGTVT và Thông tư 08/2023/TT-BGTVT về kiểm định an toàn kỹ thuật xe cơ giới',
    ],
  },

  vehicle_registration_plate: {
    hub: 'Vehicle Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên thủ tục cấp biển số xe, định danh hoặc sang tên xe.' },
      { field: 'provider', desc: 'Cục Cảnh sát Giao thông - Bộ Công an.' },
      { field: 'serviceType', desc: 'Cấp, thu hồi đăng ký, biển số định danh và đấu giá biển số xe.' },
    ],
    direct_answer_text:
      'Biển số định danh và đăng ký phương tiện là quy trình quản lý biển số xe cơ giới theo mã định danh của chủ xe theo Thông tư 24/2023/TT-BCA. Biển số gắn liền với chủ xe suốt đời. Khi bán xe, chủ xe bắt buộc làm thủ tục thu hồi biển số để quản lý trên hệ thống.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Dịch Vụ Đăng Ký & Quản Lý Biển Số Xe Định Danh',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Cục Cảnh sát Giao thông - Bộ Công an',
        url: 'https://dichvucong.bocongan.gov.vn',
      },
      serviceType: 'Đăng ký xe lần đầu, cấp biển số định danh, sang tên đổi chủ và đấu giá biển số',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế biển số định danh theo Thông tư 24/2023/TT-BCA',
        summary: 'Khung pháp lý về cấp, thu hồi đăng ký và biển số xe cơ giới đường bộ.',
        detail:
          'Biển số xe được cấp và quản lý theo mã định danh của chủ xe. Đối với chủ xe là người Việt Nam thì biển số được quản lý theo số định danh cá nhân (số CCCD). Biển số 5 số đã cấp trước đây được tự động định danh cho chính chủ.',
        actionable_angle: 'Bảng phân biệt thủ tục sang tên xe cùng tỉnh và sang tên xe khác tỉnh theo quy định định danh mới.',
      },
      trust: {
        title: 'Trách nhiệm pháp lý của chủ xe định danh & Quy định thu hồi biển',
        summary: 'Không được bán xe kèm biển số (trừ trường hợp bán xe kèm biển số trúng đấu giá).',
        detail:
          'Trong thời hạn 30 ngày kể từ ngày làm giấy tờ chuyển quyền sở hữu xe, chủ xe phải làm thủ tục thu hồi đăng ký, biển số. Nếu không làm thủ tục thu hồi, chủ xe vẫn phải chịu trách nhiệm pháp lý khi xe gây tai nạn hoặc bị phạt nguội.',
        actionable_angle: 'Mức xử phạt hành chính đối với hành vi không làm thủ tục thu hồi hoặc không sang tên xe theo quy định.',
      },
      high_intent: {
        title: 'Quy chế đấu giá biển số xe đẹp theo Nghị quyết 73/2022/QH15',
        summary: 'Điều kiện tham gia và quyền lợi của người trúng đấu giá biển số ô tô.',
        detail:
          'Người trúng đấu giá biển số xe ô tô được giữ lại biển số khi chuyển quyền sở hữu xe để đăng ký cho xe khác thuộc sở hữu của mình, hoặc được bán xe kèm theo biển số trúng đấu giá cho người khác theo quy định pháp luật.',
        actionable_angle: 'Hướng dẫn nộp tiền đặt trước, quy trình trả giá trực tuyến và thời hạn hoàn tất thủ tục đăng ký xe trúng đấu giá.',
      },
    },
    sources: [
      'Thông tư 24/2023/TT-BCA quy định về cấp, thu hồi đăng ký, biển số xe cơ giới',
      'Nghị quyết 73/2022/QH15 về thí điểm đấu giá biển số xe ô tô',
      'Nghị định 39/2023/NĐ-CP quy định chi tiết một số điều Nghị quyết 73/2022/QH15',
    ],
  },

  vehicle_toll: {
    hub: 'Vehicle Hub',
    schema_type: 'PaymentService',
    schema_category: 'https://schema.org/PaymentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên dịch vụ thu phí tự động không dừng (ETC) hoặc phí bảo trì đường bộ.' },
      { field: 'provider', desc: 'Đơn vị cung cấp dịch vụ thu phí (VETC, VDTC - ePass).' },
      { field: 'serviceType', desc: 'Thu phí sử dụng đường bộ tự động không dừng tại các trạm BOT.' },
    ],
    direct_answer_text:
      'Thu phí không dừng (ETC) và phí đường bộ là phương thức thu phí tự động bằng công nghệ RFID tại các trạm BOT toàn quốc theo Quyết định 19/2020/QĐ-TTg. Xe dán thẻ ePass hoặc VETC được thanh toán tự động qua tài khoản giao thông, giảm ùn tắc và minh bạch lộ trình.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'PaymentService',
      name: 'Dịch Vụ Thu Phí Không Dừng ETC & Phí Đường Bộ',
      provider: {
        '@type': 'Organization',
        name: 'Công ty TNHH Thu phí tự động VETC & Công ty CP Giao thông số Việt Nam (ePass)',
      },
      serviceType: 'Thu phí tự động không dừng tại trạm BOT và nộp phí sử dụng đường bộ',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quyết định 19/2020/QĐ-TTg về thu phí dịch vụ sử dụng đường bộ không dừng',
        summary: 'Khung pháp lý bắt buộc 100% các tuyến cao tốc áp dụng thu phí hoàn toàn tự động.',
        detail:
          'Tất cả các tuyến cao tốc trên toàn quốc chỉ phục vụ phương tiện có dán thẻ thu phí tự động và có đủ số dư trong tài khoản thu phí. Hành vi đi vào làn thu phí tự động khi không đủ điều kiện sẽ bị xử phạt theo Nghị định 168/2024/NĐ-CP.',
        actionable_angle: 'Mức xử phạt từ 2-3 triệu đồng và tước bằng lái xe từ 1-3 tháng đối với lỗi đi sai làn ETC khi không đủ số dư.',
      },
      trust: {
        title: 'Liên thông tài khoản giao thông VETC - ePass & Bảo mật thanh toán',
        summary: 'Cơ chế một tài khoản lưu thông thông suốt trên toàn bộ hệ thống trạm BOT toàn quốc.',
        detail:
          'Thẻ VETC và ePass được liên thông toàn diện, cho phép xe dán một trong hai loại thẻ lưu thông qua mọi trạm thu phí BOT trên cả nước mà không cần đổi thẻ. Dữ liệu trừ tiền được ghi nhận theo thời gian thực và có hóa đơn điện tử đối soát.',
        actionable_angle: 'Quy trình kiểm tra tính toàn vẹn của chip RFID dán trên kính/đèn xe và khắc phục lỗi không nhận diện thẻ.',
      },
      high_intent: {
        title: 'Biểu phí sử dụng đường bộ theo Thông tư 70/2021/TT-BTC & Nạp tiền tài khoản ETC',
        summary: 'Bảng mức thu phí bảo trì đường bộ theo chu kỳ kiểm định kỹ thuật phương tiện.',
        detail:
          'Cung cấp bảng mức thu phí sử dụng đường bộ đối với xe con, xe tải, xe khách theo biểu phí nhà nước quy định, kèm hướng dẫn nạp tiền trực tiếp vào tài khoản giao thông VETC/ePass qua ví MoMo không mất phí giao dịch.',
        actionable_angle: 'Bảng đối chiếu mức thu phí tại các tuyến cao tốc huyết mạch (Hà Nội - Hải Phòng, Pháp Vân - Cầu Giẽ, Long Thành - Dầu Giây).',
      },
    },
    sources: [
      'Quyết định 19/2020/QĐ-TTg của Thủ tướng Chính phủ về thu phí tự động không dừng',
      'Thông tư 70/2021/TT-BTC quy định mức thu, chế độ thu, nộp phí sử dụng đường bộ',
      'Nghị định 168/2024/NĐ-CP quy định xử phạt vi phạm hành chính trật tự ATGT đường bộ',
    ],
  },

  vehicle_service: {
    hub: 'Vehicle Hub',
    schema_type: 'AutomotiveBusiness',
    schema_category: 'https://schema.org/AutomotiveBusiness',
    mandatory_fields: [
      { field: 'name', desc: 'Tên trạm dịch vụ, garage hoặc điểm cung ứng nhiên liệu, trạm sạc.' },
      { field: 'provider', desc: 'Hệ thống garage, đại lý xăng dầu hoặc trạm sạc xe điện đạt chuẩn.' },
      { field: 'priceRange', desc: 'Khoảng giá dịch vụ bảo dưỡng, sửa chữa hoặc đơn giá nhiên liệu niêm yết.' },
    ],
    direct_answer_text:
      'Dịch vụ kỹ thuật phương tiện và nhiên liệu gồm mạng lưới trạm xăng dầu, trạm sạc điện, garage bảo dưỡng, cứu hộ và bãi đỗ xe phục vụ người tham gia giao thông. Giá bán lẻ xăng dầu được liên Bộ Công Thương - Tài chính điều hành định kỳ theo cơ chế thị trường.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'AutomotiveBusiness',
      name: 'Dịch Vụ Kỹ Thuật Phương Tiện & Trạm Nhiên Liệu',
      provider: {
        '@type': 'Organization',
        name: 'Mạng lưới Đối tác Giao thông & Năng lượng MoMo',
      },
      priceRange: 'Niêm yết theo đơn giá thị trường và kỳ điều hành xăng dầu Nhà nước',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Cơ chế điều hành giá xăng dầu theo Nghị định 80/2023/NĐ-CP',
        summary: 'Quy định kỳ điều hành giá bán lẻ xăng dầu vào thứ Năm hàng tuần của Liên Bộ.',
        detail:
          'Giá xăng RON 95, E5 RON 92 và dầu Diesel được công bố công khai, minh bạch căn cứ trên biến động giá thành phẩm thế giới và Quỹ Bình ổn giá xăng dầu (BOG) theo Nghị định 83/2014/NĐ-CP, Nghị định 95/2021/NĐ-CP và Nghị định 80/2023/NĐ-CP.',
        actionable_angle: 'Bảng đối chiếu giá xăng dầu vùng 1 và vùng 2 được niêm yết bởi các doanh nghiệp đầu mối (Petrolimex, PVOIL).',
      },
      trust: {
        title: 'Tiêu chuẩn kỹ thuật garage bảo dưỡng & Quy chuẩn trạm sạc xe điện',
        summary: 'Chứng nhận cơ sở bảo hành, bảo dưỡng ô tô theo Nghị định 116/2017/NĐ-CP.',
        detail:
          'Các cơ sở garage đạt chuẩn phải có giấy chứng nhận cơ sở bảo hành, bảo dưỡng của Cục Đăng kiểm, trang bị máy đọc lỗi chuẩn đoán OBD và cam kết sử dụng phụ tùng chính hãng có nguồn gốc xuất xứ rõ ràng.',
        actionable_angle: 'Checklist 8 hạng mục kiểm tra phụ tùng thay thế và tem kiểm định cột đo nhiên liệu chống gian lận.',
      },
      high_intent: {
        title: 'Lịch bảo dưỡng định kỳ theo số km & Bản đồ cứu hộ lưu động 24/7',
        summary: 'Khung mốc bảo dưỡng định kỳ 5.000km, 10.000km, 20.000km và 40.000km.',
        detail:
          'Cung cấp danh mục các công việc bảo dưỡng cấp nhỏ, cấp trung và cấp lớn cho ô tô/xe máy, kèm theo mạng lưới số điện thoại cứu hộ giao thông khẩn cấp hỗ trợ kéo xe, kích bình ắc quy và vá lốp lưu động.',
        actionable_angle: 'Bảng ước tính chi phí bảo dưỡng từng cấp độ và hướng dẫn tìm kiếm trạm sạc xe điện nhanh gần nhất.',
      },
    },
    sources: [
      'Nghị định 80/2023/NĐ-CP sửa đổi Nghị định 95/2021/NĐ-CP và Nghị định 83/2014/NĐ-CP về kinh doanh xăng dầu',
      'Nghị định 116/2017/NĐ-CP quy định điều kiện dịch vụ bảo hành bảo dưỡng ô tô',
    ],
  },

  insurtech_motor: {
    hub: 'Insurtech Hub',
    schema_type: 'InsuranceProduct',
    schema_category: 'https://schema.org/InsuranceProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói bảo hiểm xe máy hoặc ô tô (Bắt buộc TNDS hoặc Tự nguyện vật chất).' },
      { field: 'provider', desc: 'Doanh nghiệp bảo hiểm phi nhân thọ được Bộ Tài chính cấp phép.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Biểu phí bảo hiểm niêm yết theo quy định nhà nước.' },
    ],
    direct_answer_text:
      'Bảo hiểm trách nhiệm dân sự bắt buộc của chủ xe cơ giới là bảo hiểm luật định bồi thường thiệt hại về sức khỏe, tính mạng và tài sản cho bên thứ ba. Mức trách nhiệm bảo hiểm về người tối đa 150 triệu đồng mỗi vụ theo Nghị định 67/2023/NĐ-CP của Chính phủ.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'InsuranceProduct',
      name: 'Bảo Hiểm Bắt Buộc Trách Nhiệm Dân Sự Chủ Xe Cơ Giới',
      provider: {
        '@type': 'InsuranceAgency',
        name: 'Tổng công ty Bảo hiểm Bảo Việt & Bảo hiểm Bưu điện (PTI)',
      },
      feesAndCommissionsSpecification: 'Phí bảo hiểm theo biểu phí cố định quy định tại Nghị định 67/2023/NĐ-CP',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn bồi thường theo Nghị định 67/2023/NĐ-CP của Chính phủ',
        summary: 'Khung pháp lý về bảo hiểm bắt buộc TNDS của chủ xe ô tô và xe máy.',
        detail:
          'Quy định rõ mức bồi thường tối đa: Về sức khỏe, tính mạng là 150.000.000 VNĐ/người/vụ; về tài sản là 50.000.000 VNĐ/vụ đối với xe máy và 100.000.000 VNĐ/vụ đối với ô tô. Doanh nghiệp bảo hiểm phải tạm ứng bồi thường trong vòng 3 ngày làm việc kể từ khi nhận được thông báo tai nạn.',
        actionable_angle: 'Bảng chi tiết tỷ lệ thương tật chi trả bồi thường và các điểm loại trừ trách nhiệm bảo hiểm.',
      },
      trust: {
        title: 'Hiệu lực pháp lý của Giấy chứng nhận bảo hiểm điện tử',
        summary: 'Giấy chứng nhận điện tử có giá trị tương đương bản giấy khi CSGT kiểm tra.',
        detail:
          'Chủ xe được xuất trình Giấy chứng nhận bảo hiểm điện tử tích hợp mã QR xác thực trên điện thoại thay cho thẻ giấy truyền thống theo đúng quy định tại Điều 10 Nghị định 67/2023/NĐ-CP.',
        actionable_angle: 'Quy trình quét mã QR tra cứu tính hợp lệ của hợp đồng bảo hiểm trên hệ thống cơ sở dữ liệu bảo hiểm.',
      },
      high_intent: {
        title: 'Quy trình hồ sơ bồi thường tai nạn & Mức xử phạt khi không có bảo hiểm',
        summary: 'Bộ hồ sơ yêu cầu chi trả bồi thường bảo hiểm nhanh gọn không cần biên bản công an.',
        detail:
          'Đối với tai nạn không có thương vong về người, doanh nghiệp bảo hiểm và các bên tự thỏa thuận giám định hiện trường để bồi thường mà không bắt buộc phải có hồ sơ tai nạn của cơ quan công an. Mức phạt lỗi không mang hoặc không có bảo hiểm là 100.000 - 200.000 VNĐ với xe máy, 400.000 - 600.000 VNĐ với ô tô.',
        actionable_angle: 'Checklist 4 bước chụp ảnh hiện trường và gọi hotline giám định bảo hiểm ngay khi xảy ra va chạm.',
      },
    },
    sources: [
      'Luật Kinh doanh bảo hiểm số 08/2022/QH15',
      'Nghị định 67/2023/NĐ-CP quy định về bảo hiểm bắt buộc TNDS của chủ xe cơ giới',
      'Nghị định 168/2024/NĐ-CP về xử phạt vi phạm hành chính trật tự ATGT đường bộ',
    ],
  },

  insurtech_social_health: {
    hub: 'Insurtech Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên chính sách an sinh (BHYT hộ gia đình, BHXH tự nguyện).' },
      { field: 'provider', desc: 'Bảo hiểm Xã hội Việt Nam.' },
      { field: 'serviceType', desc: 'Đăng ký, gia hạn thẻ BHYT và đóng tiếp BHXH tự nguyện trực tuyến.' },
    ],
    direct_answer_text:
      'Bảo hiểm Y tế và Bảo hiểm Xã hội là các chính sách an sinh xã hội trụ cột do Nhà nước tổ chức phi lợi nhuận theo Luật BHYT và Luật BHXH. Tham gia BHYT giúp chi trả từ 80% đến 100% chi phí khám chữa bệnh đúng tuyến, giảm gánh nặng tài chính khi ốm đau.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Dịch Vụ Gia Hạn BHYT & Đóng BHXH Trực Tuyến',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Bảo hiểm Xã hội Việt Nam',
        url: 'https://baohiemxahoi.gov.vn',
      },
      serviceType: 'Gia hạn thẻ BHYT hộ gia đình và đóng tiếp BHXH tự nguyện',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn mức hưởng BHYT đúng tuyến vs. Trái tuyến theo Luật BHYT',
        summary: 'Khung pháp lý về mức hưởng bảo hiểm y tế và điều kiện thông tuyến tỉnh khám chữa bệnh.',
        detail:
          'Người tham gia BHYT được quỹ chi trả 100% chi phí khi khám chữa bệnh tại tuyến xã, chi phí cho một lần khám chữa bệnh thấp hơn 15% mức lương cơ sở, hoặc khi có thời gian tham gia BHYT 5 năm liên tục trở lên và có số tiền cùng chi trả trong năm lớn hơn 6 tháng lương cơ sở.',
        actionable_angle: 'Bảng đối chiếu tỷ lệ chi trả BHYT khi chuyển tuyến và khám chữa bệnh nội trú trái tuyến tỉnh.',
      },
      trust: {
        title: 'Sử dụng thẻ BHYT điện tử trên VssID & CCCD gắn chip',
        summary: 'Khám chữa bệnh BHYT không cần xuất trình thẻ giấy theo Đề án 06.',
        detail:
          'Người bệnh được sử dụng hình ảnh thẻ BHYT trên ứng dụng VssID - Bảo hiểm xã hội số hoặc quét thẻ CCCD gắn chip tại các cơ sở y tế để làm thủ tục khám chữa bệnh BHYT nhanh chóng, minh bạch.',
        actionable_angle: 'Hướng dẫn cài đặt ứng dụng VssID và tra cứu quá trình đóng, lịch sử hưởng quyền lợi BHYT/BHXH.',
      },
      high_intent: {
        title: 'Biểu phí BHYT hộ gia đình giảm trừ theo thành viên & Mức đóng BHXH tự nguyện',
        summary: 'Chính sách giảm trừ mức đóng từ người thứ 2 trở đi trong cùng hộ gia đình.',
        detail:
          'Người thứ nhất đóng 4.5% mức lương cơ sở; người thứ 2 đóng 70%, người thứ 3 đóng 60%, người thứ 4 đóng 50%, từ người thứ 5 trở đi đóng 40% mức đóng của người thứ nhất. Mức đóng BHXH tự nguyện bằng 22% mức thu nhập tháng do người tham gia lựa chọn.',
        actionable_angle: 'Bảng tính số tiền đóng BHYT hộ gia đình cho từng thành viên và hướng dẫn nạp tiền gia hạn trực tuyến tức thì.',
      },
    },
    sources: [
      'Luật Bảo hiểm y tế số 25/2008/QH12 (sửa đổi, bổ sung bởi Luật số 46/2014/QH13)',
      'Luật Bảo hiểm xã hội số 58/2014/QH13 (và Luật Bảo hiểm xã hội số 41/2024/QH15)',
      'Nghị định 146/2018/NĐ-CP và Nghị định 75/2023/NĐ-CP quy định chi tiết thi hành Luật BHYT',
    ],
  },

  commercial_insurance: {
    hub: 'Insurtech Hub',
    schema_type: 'InsuranceProduct',
    schema_category: 'https://schema.org/InsuranceProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên sản phẩm bảo hiểm thương mại (Nhân thọ, Tai nạn, Sức khỏe, Cháy nổ).' },
      { field: 'provider', desc: 'Doanh nghiệp bảo hiểm được Bộ Tài chính cấp phép hoạt động.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Phí bảo hiểm định kỳ, quyền lợi chi trả và điều khoản loại trừ.' },
    ],
    direct_answer_text:
      'Bảo hiểm thương mại gồm bảo hiểm nhân thọ, sức khỏe, tai nạn và cháy nổ do các công ty bảo hiểm được Bộ Tài chính cấp phép theo Luật Kinh doanh Bảo hiểm. Hợp đồng bảo hiểm bảo vệ người tham gia trước các rủi ro tài chính bất ngờ với quyền lợi chi trả minh bạch.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'InsuranceProduct',
      name: 'Bảo Hiểm Thương Mại & Nhân Thọ Toàn Diện',
      provider: {
        '@type': 'InsuranceAgency',
        name: 'Doanh nghiệp Bảo hiểm được Bộ Tài chính cấp phép',
      },
      feesAndCommissionsSpecification: 'Phí bảo hiểm đóng định kỳ hàng tháng, quý hoặc năm theo độ tuổi và quyền lợi tham gia',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn Luật Kinh doanh Bảo hiểm số 08/2022/QH15 của Bộ Tài chính',
        summary: 'Khung pháp lý bảo vệ quyền lợi bên mua bảo hiểm và giám sát an toàn tài chính doanh nghiệp bảo hiểm.',
        detail:
          'Hợp đồng bảo hiểm thương mại chịu sự quản lý của Cục Quản lý, giám sát bảo hiểm - Bộ Tài chính. Luật quy định rõ nguyên tắc trung thực tuyệt đối, thời gian cân nhắc 21 ngày đối với bảo hiểm nhân thọ và nghĩa vụ giải thích rõ các điều khoản loại trừ bồi thường của đại lý.',
        actionable_angle: 'Bảng đối chiếu danh mục điều khoản loại trừ bồi thường phổ biến và thời gian chờ (waiting period) của bệnh đặc biệt.',
      },
      trust: {
        title: 'Quyền lợi 21 ngày cân nhắc & Quy trình thẩm định sức khỏe trung thực',
        summary: 'Quyền hủy hợp đồng nhận lại 100% phí bảo hiểm trong thời gian cân nhắc luật định.',
        detail:
          'Bên mua bảo hiểm có quyền từ chối tiếp tục tham gia và được hoàn lại toàn bộ phí bảo hiểm đã đóng (sau khi trừ chi phí khám sức khỏe nếu có) trong vòng 21 ngày kể từ ngày nhận được bộ hợp đồng bảo hiểm chính thức.',
        actionable_angle: 'Checklist kê khai trung thực tiền sử bệnh án gia đình và cá nhân để tránh tranh chấp từ chối chi trả sau này.',
      },
      high_intent: {
        title: 'Biểu phí bảo hiểm theo độ tuổi & Bảng phân tích quyền lợi tử vong/bệnh hiểm nghèo',
        summary: 'Minh bạch cơ cấu phân bổ giữa chi phí bảo hiểm thuần và giá trị hoàn lại của hợp đồng.',
        detail:
          'Phân tích rõ sự khác biệt giữa sản phẩm bảo hiểm thuần bảo vệ (phí mất đi hàng năm) và bảo hiểm liên kết đầu tư (có tích lũy giá trị hoàn lại), kèm bảng ước tính quyền lợi bảo vệ tối đa trước rủi ro ung thư và bệnh hiểm nghèo theo từng nhóm tuổi.',
        actionable_angle: 'Bảng so sánh mức phí thường niên và hạn mức quyền lợi viện phí giữa các gói bảo hiểm sức khỏe phổ biến trên thị trường.',
      },
    },
    sources: [
      'Luật Kinh doanh bảo hiểm số 08/2022/QH15',
      'Nghị định 46/2023/NĐ-CP quy định chi tiết thi hành một số điều của Luật Kinh doanh bảo hiểm',
      'Thông tư 67/2023/TT-BTC hướng dẫn một số điều của Luật Kinh doanh bảo hiểm',
    ],
  },

  cinema_movie: {
    hub: 'Cinema Hub',
    schema_type: 'MovieTheater',
    schema_category: 'https://schema.org/MovieTheater',
    mandatory_fields: [
      { field: 'name', desc: 'Tên cụm rạp hoặc phim chiếu rạp.' },
      { field: 'provider', desc: 'Hệ thống cụm rạp chiếu phim (CGV, Lotte Cinema, Galaxy, BHD, Beta...).' },
      { field: 'priceRange', desc: 'Khoảng giá vé xem phim theo tiêu chuẩn phòng chiếu (2D, 3D, IMAX).' },
    ],
    direct_answer_text:
      'Cụm rạp và lịch chiếu phim cung cấp thông tin xuất chiếu, thời lượng, bảng giá vé và sơ đồ ghế ngồi tại các rạp chiếu phim trên cả nước. Khán giả dễ dàng so sánh giá vé, chọn vị trí ngồi đẹp và đặt vé xem phim trực tuyến nhanh chóng với nhiều ưu đãi.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'MovieTheater',
      name: 'Cụm Rạp Chiếu Phim & Đặt Vé Trực Tuyến',
      provider: {
        '@type': 'Organization',
        name: 'Hệ thống Cụm Rạp Đối tác MoMo (CGV, Lotte, Galaxy, BHD, Beta)',
      },
      priceRange: '45.000 VNĐ - 250.000 VNĐ',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn phân loại độ tuổi phim theo Luật Điện ảnh số 05/2022/QH15',
        summary: 'Hệ thống phân loại độ tuổi người xem phim của Cục Điện ảnh - Bộ VHTT&DL.',
        detail:
          'Phim chiếu rạp tại Việt Nam được phân loại theo 6 mức: P (Mọi lứa tuổi), K (Dưới 13 tuổi có người giám hộ), T13 (Đủ 13 tuổi trở lên), T16 (Đủ 16 tuổi trở lên), T18 (Đủ 18 tuổi trở lên) và C (Cấm phổ biến). Rạp chiếu có quyền từ chối phục vụ khán giả không đáp ứng yêu cầu độ tuổi.',
        actionable_angle: 'Bảng đối chiếu quy định giấy tờ tùy thân hợp lệ để chứng minh độ tuổi khi vào rạp xem phim T16/T18.',
      },
      trust: {
        title: 'Chính sách hủy/đổi vé rạp & Minh bạch định dạng phòng chiếu (IMAX, 4DX, ScreenX)',
        summary: 'Quy định rõ ràng về quyền lợi hoàn hủy vé và tiêu chuẩn trải nghiệm công nghệ điện ảnh.',
        detail:
          'Làm rõ chính sách đặt vé của các rạp: Vé đã thanh toán thành công thường không hỗ trợ hoàn tiền hoặc đổi suất chiếu trừ trường hợp rạp hủy buổi chiếu do sự cố kỹ thuật. Khán giả được giải thích sự khác biệt giữa màn chiếu IMAX Laser, âm thanh Dolby Atmos và ghế đôi Sweetbox.',
        actionable_angle: 'Quy trình đối soát mã đặt vé QR tại quầy soát vé tự động không cần in vé giấy.',
      },
      high_intent: {
        title: 'Bảng so sánh giá vé xem phim giữa các cụm rạp & Lịch chiếu giờ vàng',
        summary: 'Tối ưu chi phí xem phim qua các ngày khuyến mãi cố định trong tuần.',
        detail:
          'Cung cấp bảng giá vé chi tiết cho các đối tượng học sinh - sinh viên, thành viên thân thiết và các ngày ưu đãi đồng giá (như Thứ 3 vui vẻ, Thứ 4 Member Day) của CGV, Lotte, Galaxy, Beta Cinema.',
        actionable_angle: 'Bí quyết chọn vị trí ghế ngồi trung tâm có tầm nhìn và âm thanh tối ưu nhất theo từng diện tích phòng chiếu.',
      },
    },
    sources: [
      'Luật Điện ảnh số 05/2022/QH15',
      'Thông tư 05/2023/TT-BVHTTDL quy định tiêu chí phân loại và thực hiện hiển thị cảnh báo phim',
    ],
  },

  ota_travel_transit: {
    hub: 'OTA Hub',
    schema_type: 'TravelAgency',
    schema_category: 'https://schema.org/TravelAgency',
    mandatory_fields: [
      { field: 'name', desc: 'Tên dịch vụ vé máy bay, vé tàu xe, phòng khách sạn hoặc tour du lịch.' },
      { field: 'provider', desc: 'Hãng hàng không, Tổng công ty Đường sắt Việt Nam, hãng xe khách hoặc khách sạn.' },
      { field: 'priceRange', desc: 'Khoảng giá vé hoặc giá phòng niêm yết đã bao gồm thuế, phí.' },
    ],
    direct_answer_text:
      'Dịch vụ du lịch và vé vận tải trực tuyến cung cấp nền tảng tìm kiếm, đặt chỗ vé máy bay, tàu hỏa, xe khách và phòng khách sạn trong nước lẫn quốc tế. Người dùng dễ dàng so sánh lịch trình, mức giá trọn gói và thanh toán an toàn với vé điện tử tức thì.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'TravelAgency',
      name: 'Nền Tảng Đặt Vé Du Lịch & Vận Tải Trực Tuyến',
      provider: {
        '@type': 'Organization',
        name: 'Hệ thống Đối tác Hàng không, Đường sắt & Khách sạn Toàn cầu',
      },
      priceRange: 'Niêm yết giá vé minh bạch bao gồm thuế và phí sân bay/dịch vụ',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế bảo vệ hành khách hàng không & Đường sắt Việt Nam',
        summary: 'Quy định về bồi thường ứng tiền trước không hoàn lại khi chuyến bay bị chậm, hủy.',
        detail:
          'Hành khách đi máy bay được bảo vệ theo Thông tư 19/2023/TT-BGTVT của Bộ GTVT: Chậm từ 2 giờ phải phục vụ nước uống, chậm từ 4 giờ phải phục vụ ăn, chậm từ 5 giờ phải hoàn tiền vé hoặc đổi chuyến bay theo yêu cầu của khách.',
        actionable_angle: 'Bảng mức tiền bồi thường hủy chuyến bay nội địa và quốc tế theo chiều dài chặng bay.',
      },
      trust: {
        title: 'Minh bạch giá vé trọn gói: Bóc tách thuế VAT, phí sân bay & Phí dịch vụ',
        summary: 'Cam kết không phụ thu phí ẩn ngoài giá hiển thị cuối cùng trước khi bấm thanh toán.',
        detail:
          'Hiển thị đầy đủ cơ cấu giá vé máy bay gồm: Giá cước cơ bản, thuế VAT, phí an ninh soi chiếu, phí sử dụng dịch vụ cảng hàng không và phụ thu xăng dầu, tránh tình trạng giá hiển thị thấp nhưng đội giá khi checkout.',
        actionable_angle: 'Quy trình kiểm tra mã đặt chỗ (PNR) trực tiếp trên website chính hãng hàng không hoặc Đường sắt Việt Nam.',
      },
      high_intent: {
        title: 'Quy định hành lý xách tay/ký gửi & Thủ tục nhập cảnh, visa du lịch',
        summary: 'Thông tin trọng lượng hành lý tiêu chuẩn và điều kiện miễn thị thực các quốc gia phổ biến.',
        detail:
          'Làm rõ kích thước và trọng lượng hành lý xách tay chuẩn 7kg - 10kg, quy định về chất lỏng mang lên máy bay, cùng danh sách các quốc gia miễn visa cho hộ chiếu Việt Nam (ASEAN) và thủ tục xin E-visa các nước châu Á.',
        actionable_angle: 'Bảng đối chiếu phí mua thêm hành lý ký gửi trước chuyến bay vs. mua tại quầy sân bay.',
      },
    },
    sources: [
      'Luật Hàng không dân dụng Việt Nam số 66/2006/QH11 và Luật sửa đổi số 61/2014/QH13',
      'Thông tư 19/2023/TT-BGTVT quy định bồi thường ứng tiền trước không hoàn lại trong vận chuyển hành khách bằng đường hàng không',
      'Quy định vận chuyển hành khách của Tổng công ty Đường sắt Việt Nam (VNR)',
    ],
  },

  telco_data_sim: {
    hub: 'Telco Hub',
    schema_type: 'Product',
    schema_category: 'https://schema.org/Product',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói cước 4G/5G, mệnh giá nạp tiền hoặc sản phẩm eSIM du lịch.' },
      { field: 'provider', desc: 'Nhà mạng viễn thông được cấp phép (Viettel, Vinaphone, MobiFone, Wintel...).' },
      { field: 'offers', desc: 'Giá gói cước, dung lượng data và thời hạn sử dụng.' },
    ],
    direct_answer_text:
      'Dịch vụ viễn thông và data 4G/5G hỗ trợ người dùng nạp tiền điện thoại, đăng ký gói cước dữ liệu tốc độ cao và kích hoạt eSIM du lịch quốc tế tiện lợi. Các gói cước kết nối trực tiếp với nhà mạng, đảm bảo nhận data tức thì và áp dụng ưu đãi chiết khấu.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Product',
      name: 'Gói Cước Data 4G/5G & Nạp Tiền Điện Thoại',
      provider: {
        '@type': 'Organization',
        name: 'Các Nhà Mạng Viễn Thông Viettel, Vinaphone, MobiFone',
      },
      offers: {
        '@type': 'Offer',
        priceCurrency: 'VND',
        availability: 'https://schema.org/InStock',
      },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn quản lý thuê bao chính chủ theo Nghị định 49/2017/NĐ-CP',
        summary: 'Quy định bắt buộc chuẩn hóa thông tin thuê bao di động trùng khớp với CSDL Quốc gia về dân cư.',
        detail:
          'Mọi thuê bao di động phải đăng ký thông tin chính chủ bằng CCCD gắn chip để tránh bị khóa liên lạc 1 chiều, 2 chiều và thu hồi số viễn thông theo quy định của Bộ Thông tin và Truyền thông.',
        actionable_angle: 'Cú pháp nhắn tin TTTB gửi 1414 kiểm tra thông tin chính chủ miễn phí trên mọi nhà mạng.',
      },
      trust: {
        title: 'Chính sách nạp tiền trực tiếp & Bảo hành gói data/eSIM xuyên biên giới',
        summary: 'Cam kết không trừ tiền sai lệch và hỗ trợ kỹ thuật cài đặt APN eSIM 24/7.',
        detail:
          'Giao dịch nạp tiền điện thoại và gia hạn gói cước data được xử lý qua kênh kết nối API trực tiếp với nhà mạng, đảm bảo cộng tiền và lưu lượng data trong vòng 30 giây kèm hóa đơn giao dịch điện tử.',
        actionable_angle: 'Hướng dẫn cài đặt eSIM quốc tế bằng mã QR và cấu hình chuyển vùng dữ liệu (Data Roaming).',
      },
      high_intent: {
        title: 'Bảng so sánh dung lượng các gói cước Data ngày vs. Data tháng',
        summary: 'Tối ưu hóa chi phí sử dụng internet di động theo nhu cầu thực tế.',
        detail:
          'Cung cấp bảng so sánh chi tiết dung lượng tốc độ cao (1GB/ngày, 2GB/ngày, 4GB/ngày), chính sách hạ băng thông khi hết dung lượng và thời hạn sử dụng của các gói cước hot nhất trên thị trường.',
        actionable_angle: 'Bảng cú pháp đăng ký, hủy gia hạn tự động và kiểm tra lưu lượng data còn lại của từng nhà mạng.',
      },
    },
    sources: [
      'Luật Viễn thông số 24/2023/QH15',
      'Nghị định 49/2017/NĐ-CP sửa đổi, bổ sung Điều 15 Nghị định 25/2011/NĐ-CP về quản lý thuê bao di động',
    ],
  },

  hospital_health: {
    hub: 'Hospital Hub',
    schema_type: 'MedicalOrganization',
    schema_category: 'https://schema.org/MedicalOrganization',
    mandatory_fields: [
      { field: 'name', desc: 'Tên bệnh viện, cơ sở khám bệnh hoặc công cụ sức khỏe.' },
      { field: 'provider', desc: 'Cơ sở y tế được Bộ Y tế cấp giấy phép hoạt động khám chữa bệnh.' },
      { field: 'medicalSpecialty', desc: 'Chuyên khoa khám chữa bệnh hoặc mục tiêu dinh dưỡng y khoa.' },
    ],
    direct_answer_text:
      'Cổng thông tin y tế và bệnh viện hỗ trợ người dân tra cứu chuyên khoa, đặt lịch khám trực tuyến và sử dụng công cụ tính chỉ số sức khỏe như BMI chuẩn y khoa. Tiện ích giúp chủ động quản lý thời gian khám bệnh, giảm chờ đợi và theo dõi thể trạng cơ thể.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'MedicalOrganization',
      name: 'Cổng Đặt Lịch Khám Bệnh & Tiện Ích Sức Khỏe',
      provider: {
        '@type': 'MedicalOrganization',
        name: 'Hệ thống Bệnh viện & Phòng khám Đối tác Y tế',
      },
      medicalSpecialty: 'Đa khoa và Chăm sóc Sức khỏe Cộng đồng',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn khám bệnh theo Luật Khám bệnh, chữa bệnh số 15/2023/QH15',
        summary: 'Khung pháp lý về hoạt động khám bệnh, chứng chỉ hành nghề và quyền lợi người bệnh.',
        detail:
          'Người bệnh được quyền được tôn trọng danh dự, bảo vệ bí mật thông tin bệnh án và được cung cấp thông tin, giải thích đầy đủ về tình trạng bệnh, phương pháp điều trị cùng các rủi ro y khoa có thể xảy ra theo luật định.',
        actionable_angle: 'Quy trình tiếp đón người bệnh và quy định sử dụng thẻ BHYT khi đặt lịch khám trực tuyến.',
      },
      trust: {
        title: 'Công thức tính BMI, Calo chuẩn theo Viện Dinh dưỡng Quốc gia & WHO',
        summary: 'Tính toán chỉ số khối cơ thể dựa trên chuẩn thể trạng người châu Á (WPRO).',
        detail:
          'Chỉ số BMI chuẩn cho người trưởng thành châu Á: Thiếu cân (dưới 18.5), Bình thường (18.5 - 22.9), Thừa cân (23.0 - 24.9), Béo phì (từ 25.0 trở lên). Cung cấp cảnh báo dinh dưỡng khoa học, không thay thế cho chẩn đoán y khoa của bác sĩ.',
        actionable_angle: 'Ma trận đối chiếu mức tiêu hao calo TDEE theo cường độ vận động và mục tiêu kiểm soát cân nặng an toàn.',
      },
      high_intent: {
        title: 'Bảng giá viện phí khám tự nguyện vs. Khám BHYT & Hướng dẫn nhịn ăn xét nghiệm',
        summary: 'Minh bạch chi phí dịch vụ khám theo yêu cầu tại các bệnh viện công lập và tư nhân.',
        detail:
          'Cung cấp bảng giá khám giáo sư, khám chuyên khoa và các lưu ý chuẩn bị trước khi lấy mẫu máu xét nghiệm (nhịn ăn 8-12 tiếng, không uống nước ngọt) để đảm bảo kết quả xét nghiệm sinh hóa máu chuẩn xác.',
        actionable_angle: 'Checklist 5 giấy tờ tùy thân cần mang theo và sơ đồ hướng dẫn gửi xe tại các bệnh viện lớn.',
      },
    },
    sources: [
      'Luật Khám bệnh, chữa bệnh số 15/2023/QH15',
      'Tiêu chuẩn đánh giá thể trạng dinh dưỡng người châu Á của Tổ chức Y tế Thế giới (WHO WPRO)',
      'Khuyến nghị dinh dưỡng cho người Việt Nam của Viện Dinh dưỡng Quốc gia',
    ],
  },

  student_education: {
    hub: 'Student Hub',
    schema_type: 'EducationalOrganization',
    schema_category: 'https://schema.org/EducationalOrganization',
    mandatory_fields: [
      { field: 'name', desc: 'Tên trường đại học, học viện, ngành đào tạo hoặc thông tin điểm chuẩn.' },
      { field: 'provider', desc: 'Cơ sở giáo dục đại học được Bộ Giáo dục và Đào tạo cấp phép hoạt động.' },
      { field: 'description', desc: 'Đề án tuyển sinh, mức học phí và tiêu chuẩn xét tuyển đầu vào.' },
    ],
    direct_answer_text:
      'Cổng thông tin tuyển sinh và đời sống sinh viên cung cấp dữ liệu chính thống về điểm chuẩn, học phí, đề án tuyển sinh đại học và thông tin nhà trọ an toàn. Hệ thống giúp học sinh và phụ huynh định hướng ngành nghề, so sánh phương thức xét tuyển và chuẩn bị hành trang học tập.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'EducationalOrganization',
      name: 'Cổng Thông Tin Tuyển Sinh & Đời Sống Sinh Viên',
      provider: {
        '@type': 'EducationalOrganization',
        name: 'Hệ thống Các Trường Đại học & Cao đẳng Toàn quốc',
      },
      description: 'Tra cứu điểm chuẩn tuyển sinh THPT, học phí và đề án tuyển sinh chính thức',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế tuyển sinh đại học, cao đẳng theo quy định của Bộ Giáo dục & Đào tạo',
        summary: 'Căn cứ pháp lý về quy trình lọc ảo, đăng ký nguyện vọng và phương thức xét tuyển sớm.',
        detail:
          'Thí sinh đăng ký xét tuyển đại học trực tuyến trên hệ thống chung của Bộ GD&ĐT (thisinh.thitotnghiepthpt.edu.vn). Các phương thức xét tuyển sớm (học bạ, đánh giá năng lực) phải được xác nhận nguyện vọng trên cổng chung để được công nhận trúng tuyển chính thức.',
        actionable_angle: 'Bảng quy đổi điểm chứng chỉ ngoại ngữ quốc tế (IELTS/TOEFL) sang thang điểm 10 theo từng khối ngành.',
      },
      trust: {
        title: 'Minh bạch khung học phí theo Nghị định 81/2021/NĐ-CP & Nghị định 97/2023/NĐ-CP',
        summary: 'Quy định trần học phí công lập và lộ trình tăng học phí của các cơ sở giáo dục tự chủ.',
        detail:
          'Trường đại học bắt buộc phải công khai đề án tuyển sinh, chỉ tiêu, chi phí đào tạo và mức học phí dự kiến cho từng năm học của khóa học theo Thông tư 08/2022/TT-BGDĐT nhằm bảo vệ quyền lợi minh bạch tài chính cho người học.',
        actionable_angle: 'Checklist 6 tiêu chí kiểm tra độ tin cậy của hợp đồng thuê phòng trọ sinh viên tránh bẫy cọc tiền.',
      },
      high_intent: {
        title: 'Tra cứu điểm chuẩn qua các năm & Công cụ tính điểm xét tuyển tốt nghiệp',
        summary: 'Đối chiếu phổ điểm kỳ thi tốt nghiệp THPT và dự báo ngưỡng điểm trúng tuyển an toàn.',
        detail:
          'Cung cấp bảng tổng hợp điểm chuẩn 3 năm gần nhất của các ngành hot (Công nghệ thông tin, Kinh tế, Y dược), kèm công cụ tính toán điểm xét tốt nghiệp THPT tự động theo đúng trọng số môn học.',
        actionable_angle: 'Chiến thuật sắp xếp thứ tự nguyện vọng theo 3 nhóm: An toàn, Vừa sức và Thử thách.',
      },
    },
    sources: [
      'Luật Giáo dục Đại học số 08/2012/QH13 và Luật sửa đổi số 34/2018/QH14',
      'Nghị định 81/2021/NĐ-CP và Nghị định 97/2023/NĐ-CP về cơ chế thu, quản lý học phí',
      'Thông tư 08/2022/TT-BGDĐT ban hành Quy chế tuyển sinh đại học',
    ],
  },

  lottery_vietlott: {
    hub: 'Lottery Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Tên loại hình xổ số kiến thiết hoặc sản phẩm xổ số điện toán.' },
      { field: 'provider', desc: 'Công ty TNHH MTV Xổ số điện toán Việt Nam (Vietlott) hoặc Hội đồng XSKT.' },
      { field: 'serviceType', desc: 'Tra cứu kết quả mở thưởng, cơ cấu giải thưởng và thủ tục lĩnh thưởng.' },
    ],
    direct_answer_text:
      'Xổ số kiến thiết và xổ số điện toán Vietlott là hình thức vui chơi có thưởng do doanh nghiệp nhà nước trực thuộc Bộ Tài chính phát hành nhằm huy động nguồn thu phúc lợi xã hội. Người chơi có thể tra cứu kết quả mở thưởng minh bạch và quy trình lĩnh thưởng hợp pháp.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Tra Cứu Kết Quả Xổ Số & Vietlott Chính Thức',
      provider: {
        '@type': 'GovernmentOrganization',
        name: 'Công ty TNHH MTV Xổ số Điện toán Việt Nam (Vietlott) & Các Công ty XSKT',
        url: 'https://vietlott.vn',
      },
      serviceType: 'Tra cứu kết quả mở thưởng xổ số truyền thống và xổ số điện toán Vietlott',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn kinh doanh xổ số theo Thông tư 75/2013/TT-BTC & Thông tư 136/2013/TT-BTC',
        summary: 'Khung pháp lý điều chỉnh hoạt động phát hành xổ số truyền thống và xổ số điện toán.',
        detail:
          'Bộ Tài chính quản lý thống nhất hoạt động kinh doanh xổ số. Quá trình quay số mở thưởng được tiến hành công khai, minh bạch dưới sự giám sát của Hội đồng Giám sát xổ số theo đúng quy định pháp luật.',
        actionable_angle: 'Bảng đối chiếu cơ cấu giải thưởng và xác suất trúng thưởng giữa Mega 6/45, Power 6/55 và XSKT truyền thống.',
      },
      trust: {
        title: 'Nghĩa vụ nộp thuế TNCN trúng thưởng theo Luật Thuế Thu nhập cá nhân',
        summary: 'Quy định khấu trừ thuế 10% tại nguồn đối với phần giá trị giải thưởng vượt trên 10 triệu đồng.',
        detail:
          'Người trúng giải có giá trị trên 10.000.000 VNĐ cho một vé số phải nộp thuế TNCN với thuế suất 10% trên phần vượt 10 triệu đồng theo Thông tư 111/2013/TT-BTC. Doanh nghiệp xổ số có trách nhiệm khấu trừ thuế trước khi trả thưởng cho người nhận giải.',
        actionable_angle: 'Công thức tính chính xác số tiền thuế TNCN phải nộp khi trúng giải Jackpot Vietlott hoặc giải Đặc biệt XSKT.',
      },
      high_intent: {
        title: 'Thời hạn lĩnh thưởng 60 ngày & Điều kiện bảo quản vé số hợp lệ',
        summary: 'Quy định bắt buộc về hình thức vé số còn nguyên vẹn, không rách rời chắp vá.',
        detail:
          'Vé trúng thưởng phải còn nguyên hình, nguyên khổ, không rách rời, không chắp vá, không tẩy xóa. Thời hạn lĩnh thưởng tối đa là 60 ngày kể từ ngày xác định kết quả mở thưởng; quá thời hạn trên, vé trúng thưởng không còn giá trị lĩnh thưởng và số tiền giải thưởng được nộp vào ngân sách nhà nước.',
        actionable_angle: 'Địa chỉ các điểm đại lý, chi nhánh trả thưởng ủy quyền chính thức và quy trình bảo mật danh tính khi nhận giải thưởng lớn.',
      },
    },
    sources: [
      'Thông tư 75/2013/TT-BTC hướng dẫn chi tiết về hoạt động kinh doanh xổ số',
      'Thông tư 136/2013/TT-BTC hướng dẫn hoạt động kinh doanh xổ số tự chọn số điện toán',
      'Thông tư 111/2013/TT-BTC hướng dẫn thực hiện Luật Thuế TNCN về thuế thu nhập từ trúng thưởng',
    ],
  },

  entertainment_topup: {
    hub: 'Entertainment Hub',
    schema_type: 'Product',
    schema_category: 'https://schema.org/Product',
    mandatory_fields: [
      { field: 'name', desc: 'Tên thẻ game, gói nạp tiền vật phẩm hoặc tiền ảo ứng dụng chính hãng.' },
      { field: 'provider', desc: 'Nhà phát hành game hoặc nền tảng dịch vụ giải trí (VNG, Garena, Funtap, TikTok...).' },
      { field: 'offers', desc: 'Mệnh giá nạp thẻ và chính sách chiết khấu, khuyến mại.' },
    ],
    direct_answer_text:
      'Dịch vụ nạp thẻ game và ứng dụng giải trí cung cấp giải pháp mua thẻ Zing, Garena, Vcoin và nạp xu trực tiếp vào tài khoản game chính hãng qua cổng MoMo. Người dùng nhận mã thẻ hoặc nạp trực tiếp tức thì với tính bảo mật cao và mức chiết khấu cạnh tranh.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Product',
      name: 'Dịch Vụ Nạp Thẻ Game & Nền Tảng Giải Trí',
      provider: {
        '@type': 'Organization',
        name: 'Hệ thống Nhà Phát Hành Game Đối tác (Garena, VNG, Funtap, TikTok)',
      },
      offers: {
        '@type': 'Offer',
        priceCurrency: 'VND',
        availability: 'https://schema.org/InStock',
      },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn phát hành trò chơi điện tử theo Nghị định 72/2013/NĐ-CP & Nghị định 147/2024/NĐ-CP',
        summary: 'Khung pháp lý về quản lý, cung cấp và sử dụng dịch vụ Internet và trò chơi điện tử trên mạng.',
        detail:
          'Dịch vụ thanh toán kết nối trực tiếp với các trò chơi điện tử G1 đã được Bộ Thông tin và Truyền thông cấp quyết định phê duyệt nội dung, kịch bản, tuân thủ giới hạn thời gian chơi game của người dưới 18 tuổi.',
        actionable_angle: 'Bảng đối chiếu danh mục nhà phát hành game được cấp phép hoạt động chính thức tại Việt Nam.',
      },
      trust: {
        title: 'Kênh nạp chính hãng trực tiếp & Cảnh báo bẫy lừa đảo nạp game lậu',
        summary: 'Bảo vệ tài khoản game người chơi không bị khóa do nạp tiền bẩn qua thẻ tín dụng chùa.',
        detail:
          'Nạp game qua đối tác thanh toán chính thống đảm bảo vật phẩm được cộng hợp lệ vào ID nhân vật trong game. Cảnh báo tuyệt đối không đăng nhập tài khoản vào các website nạp lậu bên ngoài để tránh bị đánh cắp thông tin hoặc bị NPH khóa tài khoản vĩnh viễn.',
        actionable_angle: 'Quy trình kiểm tra mã giao dịch đối soát với bộ phận hỗ trợ khách hàng của nhà phát hành game.',
      },
      high_intent: {
        title: 'Bảng tỷ lệ quy đổi tiền mặt sang đơn vị tiền trong game & Chiết khấu ưu đãi',
        summary: 'Tối ưu hóa giá trị nạp tiền qua các chương trình hoàn tiền và mã giảm giá.',
        detail:
          'Cung cấp bảng quy đổi minh bạch: 10.000 VNĐ đổi được bao nhiêu Quân Huy (Garena), Zing Xu (VNG) hoặc Kim Cương, so sánh mức chiết khấu khi mua mã thẻ so với nạp trực tiếp qua kho ứng dụng App Store / Google Play.',
        actionable_angle: 'Hướng dẫn cài đặt bảo mật 2 lớp cho tài khoản game và cách liên kết ví thanh toán 1 chạm không cần nhập lại mã.',
      },
    },
    sources: [
      'Nghị định 72/2013/NĐ-CP và Nghị định 147/2024/NĐ-CP về quản lý, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng',
      'Quy định dịch vụ thanh toán trò chơi điện tử trực tuyến của Bộ Thông tin và Truyền thông',
    ],
  },

  trust_fraud: {
    hub: 'Trust Hub',
    schema_type: 'Article',
    schema_category: 'https://schema.org/Article',
    mandatory_fields: [
      { field: 'headline', desc: 'Tiêu đề bài cảnh báo thủ đoạn lừa đảo và hướng dẫn phòng chống tội phạm công nghệ cao.' },
      { field: 'description', desc: 'Tóm tắt các thủ đoạn mạo danh ngân hàng, ví điện tử và phương thức báo cáo cơ quan chức năng.' },
      { field: 'author', desc: 'Tên tổ chức chuyên trách an toàn thông tin hoặc phòng chống gian lận.' },
    ],
    direct_answer_text:
      'Cảnh báo lừa đảo và báo cáo gian lận là cổng thông tin nhận diện thủ đoạn tội phạm công nghệ cao như mạo danh ngân hàng, ví điện tử hay lừa đảo việc làm online. Hệ thống hướng dẫn người dùng nguyên tắc bảo mật và quy trình tố giác tội phạm tới cơ quan chức năng.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: 'Cảnh Báo Thủ Đoạn Gian Lận & Hướng Dẫn Báo Cáo Lừa Đảo Trực Tuyến',
      description: 'Nhận diện các thủ đoạn lừa đảo qua mạng, quy trình bảo vệ tài khoản và đường dây nóng tố giác tội phạm',
      author: {
        '@type': 'Organization',
        name: 'Trung tâm Giám sát An toàn Không gian mạng Quốc gia (NCSC) & MoMo',
        url: 'https://khonggianmang.vn',
      },
      inLanguage: 'vi-VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn an toàn an ninh mạng theo Luật An ninh mạng số 24/2018/QH14',
        summary: 'Khung pháp lý về phòng chống tội phạm sử dụng mạng máy tính, viễn thông chiếm đoạt tài sản.',
        detail:
          'Hành vi lừa đảo chiếm đoạt tài sản trên không gian mạng bị xử lý hình sự theo Điều 174 và Điều 290 Bộ luật Hình sự. Người dùng được hướng dẫn cách thức thu thập chứng cứ điện tử hợp lệ (ảnh chụp màn hình, sao kê giao dịch, số tài khoản nhận tiền) để phục vụ công tác điều tra.',
        actionable_angle: 'Bảng tổng hợp các đầu mối tiếp nhận tố giác tội phạm mạng: Cục An ninh mạng (A05) và Công an địa phương.',
      },
      trust: {
        title: 'Nguyên tắc bảo mật 3 Không - 2 Có & Không cung cấp OTP trong mọi trường hợp',
        summary: 'Nhân viên ngân hàng và ví điện tử tuyệt đối không bao giờ yêu cầu khách hàng cung cấp mật khẩu hoặc mã OTP.',
        detail:
          'Nguyên tắc sống còn: Không bấm vào link lạ, Không tải app ngoài cửa hàng chính thức, Không chia sẻ mã OTP/mật khẩu; Có xác minh danh tính người gọi qua kênh chính thức và Có kiểm tra bảo mật sinh trắc học trước khi chuyển tiền.',
        actionable_angle: 'Checklist 5 dấu hiệu nhận biết tin nhắn mạo danh thương hiệu (SMS Brandname) và link độc hại có đuôi tên miền giả mạo.',
      },
      high_intent: {
        title: 'Quy trình xử lý khẩn cấp khi nghi ngờ bị lừa: Khóa tài khoản trong 60 giây',
        summary: 'Các bước hành động tức thì để phong tỏa dòng tiền và hạn chế tối đa thiệt hại tài sản.',
        detail:
          'Hướng dẫn người dùng: 1. Gọi ngay hotline tổng đài ngân hàng/ví điện tử yêu cầu khóa tài khoản khẩn cấp; 2. Đổi mật khẩu email và các tài khoản liên kết; 3. Báo cáo số tài khoản kẻ lừa đảo lên Cổng cảnh báo an toàn thông tin quốc gia (canhbao.khonggianmang.vn).',
        actionable_angle: 'Mẫu đơn trình báo lừa đảo chiếm đoạt tài sản gửi Cơ quan Cảnh sát Điều tra chuẩn pháp lý.',
      },
    },
    sources: [
      'Luật An ninh mạng số 24/2018/QH14',
      'Bộ luật Hình sự số 100/2015/QH13 (Điều 174, Điều 290)',
      'Cổng không gian mạng quốc gia - Cục An toàn thông tin, Bộ TT&TT (khonggianmang.vn)',
    ],
  },

  lifestyle_info: {
    hub: 'Lifestyle Hub',
    schema_type: 'Article',
    schema_category: 'https://schema.org/Article',
    mandatory_fields: [
      { field: 'headline', desc: 'Tiêu đề bài viết thông tin văn hóa, lịch âm hoặc tham khảo giải trí.' },
      { field: 'description', desc: 'Tóm tắt nội dung tham khảo về lịch vạn niên, tử vi hoặc chiêm tinh học dân gian.' },
      { field: 'author', desc: 'Tên tổ chức biên tập nội dung.' },
    ],
    direct_answer_text:
      'Lịch âm, tử vi và chiêm tinh học dân gian là các thông tin văn hóa truyền thống phục vụ nhu cầu tham khảo ngày giờ tốt, phong tục tập quán và giải trí lành mạnh. Các nội dung mang tính chất tham khảo đời sống tinh thần, không mang yếu tố cam kết tài chính hay mê tín.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: 'Tra Cứu Lịch Âm, Tử Vi & Văn Hóa Dân Gian',
      description: 'Thông tin tra cứu lịch vạn niên, ngày hoàng đạo và phong tục truyền thống mang tính chất tham khảo',
      author: {
        '@type': 'Organization',
        name: 'Chuyên Mục Đời Sống & Văn Hóa Dân Gian MoMo',
        url: 'https://www.momo.vn',
      },
      inLanguage: 'vi-VN',
    },
    pillars: {
      expertise: {
        title: 'Quy luật lịch pháp cổ truyền & Phương pháp tính toán thiên văn lịch âm dương',
        summary: 'Nguyên lý tính ngày sóc, tiết khí và các quy luật chuyển động thiên văn của mặt trăng và mặt trời.',
        detail:
          'Lịch âm dương Việt Nam được tính toán dựa trên các quy luật thiên văn học chuẩn xác về chu kỳ tuần trăng và 24 tiết khí trong năm, phục vụ đời sống nông nghiệp và lễ tết truyền thống của dân tộc.',
        actionable_angle: 'Bảng tra cứu 24 tiết khí trong năm và các mốc ngày lễ tết truyền thống Việt Nam.',
      },
      trust: {
        title: 'Định vị nội dung tham khảo văn hóa & Cảnh báo mê tín dị đoan',
        summary: 'Tôn trọng các nét đẹp văn hóa phong tục tập quán, kiên quyết bài trừ các hủ tục trục lợi mê tín.',
        detail:
          'Nội dung tử vi, bói bài Tarot hay Kinh dịch hoàn toàn mang tính chất tham khảo tâm lý và chiêm nghiệm văn hóa dân gian. Tuyệt đối không chi tiền cho các dịch vụ dâng sao giải hạn, bùa ngải hay các quyết định tài chính dựa trên bói toán.',
        actionable_angle: 'Bộ quy tắc tiếp cận thông tin tử vi một cách tích cực, khoa học và giữ vững tư duy duy lý trong cuộc sống.',
      },
      high_intent: {
        title: 'Bảng tra cứu ngày hoàng đạo, giờ tốt xuất hành & Lịch vạn niên chuẩn',
        summary: 'Công cụ đổi ngày dương lịch sang âm lịch và xem các khung giờ hoàng đạo trong ngày.',
        detail:
          'Cung cấp bảng lịch vạn niên trực quan, giúp người dùng tra cứu nhanh ngày âm lịch tương ứng, tuổi xung khắc và hướng xuất hành đầu năm, phục vụ việc sắp xếp công việc cá nhân thuận tiện.',
        actionable_angle: 'Hướng dẫn chuyển đổi âm - dương lịch tự động và cài đặt thông báo nhắc nhở ngày mùng một, ngày rằm hàng tháng.',
      },
    },
    sources: [
      'Nghiên cứu Lịch pháp học Việt Nam và Thiên văn học cổ đại',
      'Viện Hàn lâm Khoa học Xã hội Việt Nam - Các công trình nghiên cứu Văn hóa Dân gian Việt Nam',
    ],
  },
};

/**
 * BẢNG GÁN TƯỜNG MINH 161 THEMES VÀO ARCHETYPE CHUẨN XÁC
 * Thay thế hoàn toàn chuỗi text.includes() mơ hồ trước đây.
 * Theme nào chưa có Archetype chuẩn hóa hoặc nằm ngoài phạm vi thì gán null.
 */
export const THEME_ARCHETYPE: Record<string, ArchetypeKey | null> = {
  // ── Financial Hub (62 themes) ──
  'gui-tiet-kiem': 'financial_savings',
  'lai-suat': 'financial_savings',
  'tich-luy': 'financial_savings',
  'chung-chi-tien-gui': 'financial_savings',
  'vi-tra-sau': 'financial_credit_paylater',
  'tra-gop': 'financial_credit_paylater',
  'vay': 'financial_consumer_loan',
  'vay-tin-chap': 'financial_consumer_loan',
  'vay-the-chap': 'financial_consumer_loan',
  'tin-dung': 'financial_credit_line',
  'du-no': 'financial_credit_line',
  'thau-chi': 'financial_credit_line',
  'lai-vay': 'financial_credit_line',
  'the-tin-dung': 'financial_card_payment',
  'the-ghi-no': 'financial_card_payment',
  'the-tra-truoc': 'financial_card_payment',
  'the-visa': 'financial_card_payment',
  'master-card': 'financial_card_payment',
  'napas': 'financial_card_payment',
  'thanh-toan-qr': 'financial_card_payment',
  'chuyen-khoan': 'financial_card_payment',
  'internet-banking': 'financial_card_payment',
  'vi-dien-tu': 'financial_card_payment',
  'chung-khoan': 'financial_investment',
  'co-phieu': 'financial_investment',
  'trai-phieu': 'financial_investment',
  'chung-chi-quy': 'financial_investment',
  'quy-etf': 'financial_investment',
  'quy-mo': 'financial_investment',
  'phai-sinh': 'financial_investment',
  'ma-chung-khoan': 'financial_investment',
  'dau-tu': 'financial_investment',
  'uy-thac': 'financial_investment',
  'quy-huu-tri': 'financial_investment',
  'co-tuc': 'financial_investment',
  'ky-quy': 'financial_investment',
  'gia-vang': 'financial_gold_fx',
  'bac': 'financial_gold_fx',
  'ty-gia': 'financial_gold_fx',
  'ngoai-te': 'financial_gold_fx',
  'doi-tien': 'financial_gold_fx',
  'kieu-hoi': 'financial_gold_fx',
  'diem-tin-dung': 'financial_credit_score',
  'no-xau': 'financial_credit_score',
  'thue-tncn': 'tax_payroll',
  'ma-so-thue': 'tax_payroll',
  'giam-tru-gia-canh': 'tax_payroll',
  'tinh-luong': 'tax_payroll',
  'thue': 'tax_payroll',
  'gdp': 'macro_knowledge',
  'lam-phat': 'macro_knowledge',
  'giam-phat': 'macro_knowledge',
  'lai-kep': 'macro_knowledge',
  'ke-hoach-tai-chinh': 'macro_knowledge',
  'tu-do-tai-chinh': 'macro_knowledge',
  'quy-du-phong': 'macro_knowledge',
  'tai-san': 'macro_knowledge',
  'tieu-san': 'macro_knowledge',
  'dong-tien': 'macro_knowledge',
  'von-luu-dong': 'macro_knowledge',
  'ngan-hang': null,
  'crypto': null,

  // ── Vehicle Hub (33 themes) ──
  'phat-nguoi': 'vehicle_traffic_fines',
  'loi-giao-thong': 'vehicle_traffic_fines',
  'giay-phep-lai-xe': 'driver_license',
  'thi-bang-lai-xe': 'driver_license',
  'ly-thuyet-lai-xe': 'driver_license',
  'phan-mem-mo-phong': 'driver_license',
  'dang-kiem': 'driver_license',
  'bien-so-xe': 'vehicle_registration_plate',
  'bien-so-dep': 'vehicle_registration_plate',
  'sang-ten-xe': 'vehicle_registration_plate',
  'vetc': 'vehicle_toll',
  'epass': 'vehicle_toll',
  'phi-khong-dung': 'vehicle_toll',
  'phi-duong-bo': 'vehicle_toll',
  'gia-xang': 'vehicle_service',
  'gia-dau': 'vehicle_service',
  'tram-xang': 'vehicle_service',
  'tram-sac': 'vehicle_service',
  'doi-pin': 'vehicle_service',
  'gara-o-to': 'vehicle_service',
  'garage-keywords-list': 'vehicle_service',
  'sua-xe': 'vehicle_service',
  'rua-xe': 'vehicle_service',
  'cuu-ho-xe': 'vehicle_service',
  'bao-duong-xe': 'vehicle_service',
  'dinh-gia-xe': 'vehicle_service',
  'gia-xe': 'vehicle_service',
  'bai-do-xe': 'vehicle_service',
  'bai-giu-xe': 'vehicle_service',
  'thue-truoc-ba': 'tax_payroll',
  'chi-duong': null,
  'metro': null,
  'tuyen-xe-buyt': null,

  // ── Insurtech Hub (8 themes) ──
  'bao-hiem-xe-may': 'insurtech_motor',
  'bao-hiem-o-to': 'insurtech_motor',
  'bhyt': 'insurtech_social_health',
  'bhxh': 'insurtech_social_health',
  'bao-hiem-nhan-tho': 'commercial_insurance',
  'bao-hiem-tai-nan': 'commercial_insurance',
  'bao-hiem-chay-no': 'commercial_insurance',
  'phi-bao-hiem': 'commercial_insurance',

  // ── Cinema Hub (5 themes) ──
  'rap': 'cinema_movie',
  've-xem-phim': 'cinema_movie',
  'lich-phim': 'cinema_movie',
  'dat-phim': 'cinema_movie',
  'phim': 'cinema_movie',

  // ── OTA Hub (18 themes) ──
  've-may-bay': 'ota_travel_transit',
  've-tau': 'ota_travel_transit',
  've-xe': 'ota_travel_transit',
  've-cap-treo': 'ota_travel_transit',
  'gia-pha': 'ota_travel_transit',
  'tour-du-lich': 'ota_travel_transit',
  'du-lich': 'ota_travel_transit',
  'dat-resort': 'ota_travel_transit',
  'visa-du-lich': 'ota_travel_transit',
  'du-lich-viet-nam': 'ota_travel_transit',
  'du-lich-thai-lan': 'ota_travel_transit',
  'du-lich-nhat': 'ota_travel_transit',
  'du-lich-han-quoc': 'ota_travel_transit',
  'du-lich-trung-quoc': 'ota_travel_transit',
  'du-lich-dai-loan': 'ota_travel_transit',
  'du-lich-singapore': 'ota_travel_transit',
  'du-lich-an-do': 'ota_travel_transit',
  'du-lich-hongkong': 'ota_travel_transit',

  // ── Telco Hub (8 themes) ──
  'data-4g': 'telco_data_sim',
  'nap-tien-dien-thoai': 'telco_data_sim',
  'sim': 'telco_data_sim',
  'esim-du-lich': 'telco_data_sim',
  'sim-du-lich': 'telco_data_sim',
  'sim-thai-lan': 'telco_data_sim',
  'sim-nhat-ban': 'telco_data_sim',
  'sim-trung-quoc': 'telco_data_sim',

  // ── Hospital Hub (4 themes) ──
  'benh-vien': 'hospital_health',
  'dat-lich-kham-benh': 'hospital_health',
  'tinh-calo': 'hospital_health',
  'bmi': 'hospital_health',

  // ── Student Hub (9 themes) ──
  'dai-hoc': 'student_education',
  'cao-dang': 'student_education',
  'truong-trung-cap': 'student_education',
  'diem-chuan': 'student_education',
  'hoc-phi': 'student_education',
  'tuyen-sinh': 'student_education',
  'sinh-vien': 'student_education',
  'nha-tro': 'student_education',
  'viec-lam-sinh-vien': null,

  // ── Lottery Hub (3 themes) ──
  'xo-so': 'lottery_vietlott',
  'vietlott': 'lottery_vietlott',
  've-so': 'lottery_vietlott',

  // ── Entertainment Hub (4 themes) ──
  'nap-game': 'entertainment_topup',
  'game-app': 'entertainment_topup',
  'nph-game': 'entertainment_topup',
  'nap-tiktok': 'entertainment_topup',

  // ── Trust Hub (2 themes) ──
  'lua-dao': 'trust_fraud',
  'bao-cao-lua-dao': 'trust_fraud',

  // ── Other Hub (5 themes) ──
  'tarot': 'lifestyle_info',
  'tu-vi': 'lifestyle_info',
  'kinh-dich': 'lifestyle_info',
  'lich-am': 'lifestyle_info',
  'ma-giam-gia': null,
};

/**
 * Trả về GEO Entity Blueprint cho theme.
 * Trả về null khi theme không có Archetype phù hợp (không sinh boilerplate bừa bãi).
 */
export function getGeoEntityBlueprint(
  themeId: string,
  themeName: string,
  sector?: string
): GeoEntityBlueprint | null {
  const normId = (themeId || '').toLowerCase().trim();
  const archetypeKey = THEME_ARCHETYPE[normId];

  if (!archetypeKey) {
    return null;
  }

  const archetype = DOMAIN_ONTOLOGY_REGISTRY[archetypeKey];
  if (!archetype) {
    return null;
  }

  const directAnswer = archetype.direct_answer_text;
  const wordCount = directAnswer.trim().split(/\s+/).filter(Boolean).length;

  return {
    ...archetype,
    theme: themeName,
    word_count: wordCount,
  };
}
'''

def main():
    target_path = Path('/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/content-plan/geo-entity-registry.ts')
    target_path.write_text(TS_CONTENT, encoding='utf-8')
    print(f"Successfully generated {target_path} ({len(TS_CONTENT.splitlines())} lines)")

if __name__ == '__main__':
    main()
